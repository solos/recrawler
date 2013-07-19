#!/usr/bin/env python
#coding=utf-8

import gevent
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool

import db
import time
import json
import sched
import redis
import config
from utils import handle
from utils import extract_domain
from datetime import timedelta
from expiredict import DataCache


gpool = Pool(10)
global domain_cache
domain_cache = DataCache(timedelta(0, 10, 0))

POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)


def work(queue):
    jobs = db.get_jobs()
    r = redis.Redis(connection_pool=POOL)
    jobs = filter_recent(r, jobs)
    #print 'domain cache', [i for i in domain_cache.items()]
    #urlhash_statuses = gpool.map(handle, jobs)
    print jobs
    gpool.map(handle, jobs)


def filter_recent(r, jobs):
    filtered_jobs = []
    for job in jobs:
        try:
            task = json.loads(job)
            url = task['url']
            domain = extract_domain(url)
        except:
            r.lpush(config.QUEUE, job)

        try:
            domain_cache[domain]
            r.lpush(config.QUEUE, job)
        except KeyError:
            domain_cache.set(domain, None, timedelta(0, 10, 0))
            filtered_jobs.append(job)
    return filtered_jobs


def cycle_run(interval):
    s.enter(interval, 0, cycle_run, (interval,))
    work('default')


if __name__ == '__main__':
    interval = 10
    s = sched.scheduler(time.time, gevent.sleep)
    s.enter(interval, 0, cycle_run, (interval, ))
    s.run()
