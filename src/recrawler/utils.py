#!/usr/bin/env python
#coding=utf-8

import gevent
from gevent import monkey
monkey.patch_all()

import db
import json
import urllib2
import cityhash
import encoding
from spider import spider
from logger import logger
from tldextracter import extract_domain


def fetch(url, proxy=True):

    if proxy:
        opener = spider.get_proxy_opener()
    else:
        opener = spider.get_opener()
    content = ''
    status = 408
    try:
        with gevent.Timeout(5, False):
            req = opener.open(url)
            status = req.getcode()
            content = req.read()
    except urllib2.HTTPError, e:
        status = int(e.code)
    except urllib2.URLError, e:
        if isinstance(e.reason, Exception):
            status = int(e.reason.errno)
    except Exception, e:
        print e
        pass
    print 'length', len(content)
    return status, content


def process(func, *args, **kwargs):
    print 'process', args, kwargs

    def wrapper(*args, **kwargs):
        url = func(*args, **kwargs)
        print 'wrapper', args, kwargs, url
        return url
    return wrapper


@process
def handle(job, *args, **kwargs):
    print 'handle', args, kwargs
    task = json.loads(job)
    url = task["url"]
    domain = extract_domain(url)
    status, content = fetch(url, proxy=False)
    url = url.encode('utf8')
    urlhash = cityhash.CityHash64(url)
    logger.info('%s|%s' % (url, status))
    if status != 200:
        db.push(url, detail=False)
        return (url, urlhash, status, domain, content)
    _, content = encoding.html_to_unicode('', content)
    return (url, urlhash, status, domain, content)


if __name__ == '__main__':
    #pass
    job = {"url": 'http://www.baidu.com'}
    handle(json.dumps(job))
