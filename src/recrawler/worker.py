#!/usr/bin/env python
#coding=utf-8

import gevent
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool

import json
import time
import sched
import queue
import magic
import config
import fetcher
import encoding
from logger import logger

gpool = Pool(config.GPOOLSIZE)


def work():
    jobs = queue.get_jobs()
    print jobs
    gpool.map(handle, jobs)


def handle(job, *args, **kwargs):
    task = json.loads(job)
    url = task["url"]
    status, source = fetcher.fetch(url, use_proxy=False)
    logger.info('%s|%s' % (url, status))
    segment = source[:(len(source), 1024)[len(source) > 1024]]
    if magic.from_buffer(segment, mime=True) != 'text/html':
        return (url, source)
    try:
        _, source = encoding.html_to_unicode('', source)
    except Exception, e:
        print e
    return (url, source)


def cycle_run(interval):
    s.enter(interval, 0, cycle_run, (interval,))
    work()

if __name__ == '__main__':
    interval = config.INTERVAL
    s = sched.scheduler(time.time, gevent.sleep)
    s.enter(interval, 0, cycle_run, (interval, ))
    s.run()
