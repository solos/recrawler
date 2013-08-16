#!/usr/bin/env python
#coding=utf-8

import gevent
from gevent import monkey
monkey.patch_all()

import re
import db
import json
import random
import config
import requests
import cityhash
import lxml.html
from logger import logger
from proxies import PROXIES
from useragents import USER_AGENTS
from tldextracter import extract_domain
from tldextracter import extract_rootdomain
from htmlcontent import Extractor

ext = Extractor()
title_match = re.compile(r'<title>(.*?)</title>', re.IGNORECASE)


def fetch(url, use_proxy=True, timeout=None, headers={}):
    status, content = 408, ''
    timeout = timeout or config.TIMEOUT
    headers = headers or config.HEADERS
    useragent = random.randint(0, len(USER_AGENTS)-1)
    headers["user-agent"] = useragent
    if use_proxy:
        proxy_index = random.randint(0, len(PROXIES)-1)
        proxies = PROXIES[proxy_index]
        try:
            with gevent.Timeout(config.TIMEOUT, Exception):
                r = requests.get(url, stream=False, verify=False,
                                 timeout=timeout, headers=headers,
                                 proxies=proxies)
        except Exception, e:
            print e
            return status, content
    else:
        try:
            with gevent.Timeout(config.TIMEOUT, Exception):
                r = requests.get(url, stream=False, verify=False,
                                 timeout=timeout, headers=headers)
        except Exception, e:
            print e
            return status, content
    return r.status_code, r.content


def process(func):

    def wrapper(*args, **kwargs):
        url, urlhash, status, domain, content = func(*args, **kwargs)
        if not content or not isinstance(content, unicode):
            return (url, urlhash, status, domain, content)
        url = url.encode('utf8')
        content = content.encode('utf8')
        tree = lxml.html.fromstring(content)
        html = content
        ext_content = ext.get_content(content, True, with_tag=False)
        urls = map(lambda a: a.attrib['href'] if
                   a.attrib['href'].startswith('http') and
                   domain in a.attrib['href'] or
                   a.attrib['href'].startswith('/') else None,
                   filter(lambda a: 'href' in a.attrib, tree.xpath('//a')))
        urls = filter(None, urls)
        urls = map(lambda uri: 'http://%s%s' % (domain, uri) if
                   uri.startswith('/') else uri,
                   urls)
        urls = list(set(urls))
        rootdomain = extract_rootdomain(url)
        if not rootdomain:
            return (url, urlhash, status, domain, content)
        domainhash = cityhash.CityHash64(rootdomain)
        site_id, language = db.get_site_info(domainhash)
        if not site_id or not language:
            pass
        try:
            title = title_match.findall(content)[0]
        except Exception, e:
            print e
            title = ''
        print 'site_id', site_id, 'languagle', language, 'urlhash', urlhash
        print 'title', title, 'url', url, 'ext_content', ext_content
        print 'urls', urls
        try:
            db.insert_db(site_id, language, urlhash, title, url,
                         ext_content, html)
        except Exception, e:
            print e
        try:
            map(db.submit_job, urls)
        except Exception, e:
            print e
        return (url, urlhash, status, domain, content)
    return wrapper


@process
def handle(job):
    task = json.loads(job)
    url = task["url"]
    domain = extract_domain(url)
    status, content = fetch(url, use_proxy=False)
    url = url.encode('utf8')
    urlhash = cityhash.CityHash64(url)
    logger.info('%s|%s' % (url, status))
    if status != 200:
        db.push(url, detail=False)
        return (url, urlhash, status, domain, content)
    return (url, urlhash, status, domain, content)

if __name__ == '__main__':
    #pass
    job = {"url": 'http://www.baidu.com'}
    handle(json.dumps(job))
