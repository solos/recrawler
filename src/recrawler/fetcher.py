#!/usr/bin/env python
#coding=utf-8

import gevent
from gevent import monkey
monkey.patch_all()

import config
import requests

s = requests.Session()


def fetch(url, use_proxy=True, timeout=None, headers={}, **kw):
    status, content = 408, ''
    timeout = timeout or config.TIMEOUT
    headers = headers or config.HEADERS
    useragent = config.USER_AGENT
    headers["user-agent"] = useragent
    if use_proxy:
        proxies = {}
        proxy = ''
        if proxy:
            proxies = {'http': proxy}
        try:
            with gevent.Timeout(config.TIMEOUT, Exception):
                r = s.get(url, stream=False, verify=False, timeout=timeout,
                          headers=headers, proxies=proxies)
        except Exception, e:
            print e
            return status, content
    else:
        try:
            with gevent.Timeout(config.TIMEOUT, Exception):
                r = s.get(url, stream=False, verify=False, timeout=timeout,
                          headers=headers)
        except Exception, e:
            print e
            return status, content
    return r.status_code, r.content
