#!/usr/bin/env python
#coding=utf-8

from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool

import json
import queue
import config
import fetcher
import encoding
import extracter
from logger import logger

gpool = Pool(config.GPOOLSIZE)


def work():
    q = queue.Queue()
    for i in xrange(1000001, 1000020):
        q.lpush('{"url": "http://www.exmaple.com/%s"}' % i)
    jobs = q.getjobs()
    while jobs:
        for job in jobs:
            print job
            gpool.spawn(handle, job, queue=q)
        gpool.join()
        jobs = q.getjobs()


def handle(job, *args, **kwargs):
    queue = kwargs['queue']
    task = json.loads(job)
    url = task["url"]
    status, source = fetcher.fetch(url, use_proxy=False)
    logger.info('%s|%s' % (url, status))
    try:
        _, source = encoding.html_to_unicode('', source)
    except Exception, e:
        print e
    urls = extracter.extract_links(url, source)
    for i in urls:
        queue.lpush('{"url": "%s"}' % i)
    return urls

if __name__ == '__main__':
    work()
