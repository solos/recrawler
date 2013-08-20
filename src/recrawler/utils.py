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
import urlnorm
import requests
import cityhash
import encoding
import lxml.html
from logger import logger
from htmlcontent import Extractor
from proxies import PROXIES
from useragents import USER_AGENTS
from tldextracter import extract_domain
from tldextracter import extract_rootdomain
from rulers import RULERS


ext = Extractor()
title_match = re.compile(r'<title>(.*?)</title>', re.IGNORECASE)
url_match = re.compile(r'#.*', re.DOTALL)


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


def process(func, *args, **kwargs):

    def wrapper(*args, **kwargs):
        url, urlhash, status, domain, content = func(*args, **kwargs)
        if not content or not isinstance(content, unicode):
            return []
        try:
            url = url.encode('utf8')
        except Exception, e:
            print e
        rootdomain = extract_rootdomain(url)
        if not rootdomain:
            return []
        try:
            absolute_content = lxml.html.make_links_absolute(content, url)
            tree = lxml.html.fromstring(absolute_content)
        except Exception, e:
            print e
            return []
        u_content = content.encode('utf8')
        html = u_content
        try:
            ext_content = ext.get_content(content, True, with_tag=False)
        except Exception, e:
            print e
            ext_content = ''
        elems = tree.xpath('//a[@href]')
        urls = map(lambda a: a.attrib['href'], elems)
        urls = list(set(urls))
        filtered_urls = []
        for _url in urls:
            _url = url_match.sub('', _url)
            try:
                _url = urlnorm.norm(_url)
            except Exception, e:
                print e
                continue

            for prefix in RULERS[rootdomain]["rulers"]:
                if _url.startswith(prefix):
                    filtered_urls.append(_url)
                    break
        domainhash = cityhash.CityHash64(rootdomain)
        site_id, language = db.get_site_info(domainhash)
        if not site_id or not language:
            pass
        try:
            title = title_match.findall(u_content)[0]
        except Exception, e:
            print e
            title = ''
        print 'site_id', site_id, 'languagle', language, 'urlhash', urlhash
        print 'title', title, 'url', url, 'ext_content', ext_content
        print 'urls', filtered_urls

        try:
            map(db.push, filtered_urls)
        except Exception, e:
            print e

        try:
            db.insert_db(site_id, language, urlhash, title, url,
                         ext_content, html)
        except Exception, e:
            print e, type(url)

        return filtered_urls
    return wrapper


@process
def handle(job, *args, **kwargs):
    print 'handle', args, kwargs
    task = json.loads(job)
    url = task["url"]
    domain = extract_domain(url)
    status, content = fetch(url, use_proxy=False)
    url = url.encode('utf8')
    urlhash = cityhash.CityHash64(url)
    logger.info('%s|%s' % (url, status))
    _, content = encoding.html_to_unicode('', content)
    if status != 200:
        db.push(url, detail=False)
        return (url, urlhash, status, domain, content)
    return (url, urlhash, status, domain, content)


if __name__ == '__main__':
    #pass
    job = {"url": "http://tech.cnr.cn"}
    handle(json.dumps(job))
