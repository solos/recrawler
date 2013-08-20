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
from tldextracter import extract_rootdomain

gpool = Pool(config.GPOOLSIZE)
POOL = redis.ConnectionPool(host=config.RHOST,
                            port=config.RPORT,
                            db=config.RDB)


def work():
    jobs = db.get_jobs()
    r = redis.Redis(connection_pool=POOL)
    jobs = filter_recent(r, jobs)
    print jobs
    gpool.map(handle, jobs)


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
                r.expire('%s_status' % rootdomain, config.EXPIRE)
                filtered_jobs.append(job)
            else:
                r.lpush(config.QUEUE, job)
        except Exception, e:
            print e
            return jobs
    return filtered_jobs


def cycle_run(interval):
    s.enter(interval, 0, cycle_run, (interval,))
    work()


if __name__ == '__main__':
    interval = config.INTERVAL
    s = sched.scheduler(time.time, gevent.sleep)
    s.enter(interval, 0, cycle_run, (interval, ))
    s.run()
