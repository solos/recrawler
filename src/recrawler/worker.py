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
import murmur
from utils import handle
from bitarray import bitarray
from tldextracter import extract_rootdomain

gpool = Pool(10)
POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

global bitmap
bitmap = bitarray(2**32)
bitmap.setall(False)


def do(job):
    urls = handle(job)
    for url in urls:
        urlhash = murmur.string_hash(url)
        if not bitmap[urlhash]:
            bitmap[urlhash] = True
            db.push(url)


def work():
    jobs = db.get_jobs()
    r = redis.Redis(connection_pool=POOL)
    jobs = filter_recent(r, jobs)
    #print 'domain cache', [i for i in domain_cache.items()]
    #urlhash_statuses = gpool.map(handle, jobs)
    print jobs
    gpool.map(do, jobs)


def filter_recent(r, jobs):
    filtered_jobs = []
    for job in jobs:
        try:
            task = json.loads(job)
            url = task['url']
            rootdomain = extract_rootdomain(url)
        except:
            r.lpush(config.QUEUE, job)

        try:
            if not r.exists('%s_status' % rootdomain):
                r.set('%s_status' % rootdomain, '')
                r.expire('%s_status' % rootdomain, 10)
                filtered_jobs.append(job)
            else:
                r.lpush(config.QUEUE, job)
        except Exception, e:
            print e
    return filtered_jobs


def cycle_run(interval):
    s.enter(interval, 0, cycle_run, (interval,))
    work()


if __name__ == '__main__':
    interval = 10
    s = sched.scheduler(time.time, gevent.sleep)
    s.enter(interval, 0, cycle_run, (interval, ))
    s.run()
