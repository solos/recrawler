#!/usr/bin/env python
#coding=utf-8

import gevent
from gevent import monkey
monkey.patch_all()

import re
import db
import json
import urllib2
import cityhash
import encoding
import lxml.html
from spider import spider
from logger import logger
from htmlcontent import Extractor
from tldextracter import extract_domain
from tldextracter import extract_rootdomain
from rulers import RULERS


ext = Extractor()
title_match = re.compile(r'<title>(.*?)</title>', re.IGNORECASE)


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

    def wrapper(*args, **kwargs):
        url, urlhash, status, domain, content = func(*args, **kwargs)
        if not content:
            return (url, urlhash, status, domain, content)
        url = url.encode('utf8')
        rootdomain = extract_rootdomain(url)
        if not rootdomain:
            return (url, urlhash, status, domain, content)
        absolute_content = lxml.html.make_links_absolute(content, url)
        tree = lxml.html.fromstring(absolute_content)
        content = content.encode('utf8')
        html = content
        ext_content = ext.get_content(content, True, with_tag=False)
        urls = tree.xpath('//a')
        urls = filter(lambda a: 'href' in a.attrib, tree.xpath('//a'))
        urls = filter(None, urls)
        urls = map(lambda a: a.attrib['href'], urls)
        urls = filter(lambda url: not url.startswith('javascript:') and
                      not url.startswith('mailto:') and not None, urls)
        urls = list(set(urls))
        filtered_urls = []
        for url in urls:
            for prefix in RULERS[rootdomain]["rulers"]:
                try:
                    if url.startswith(prefix):
                        filtered_urls.append(url)
                except Exception, e:
                    #print e
                    continue
        domainhash = cityhash.CityHash64(rootdomain)
        site_id, language = db.get_site_info(domainhash)
        if not site_id or not language:
            print site_id, language
            pass
        try:
            title = title_match.findall(content)[0]
        except Exception, e:
            print e
            title = ''
        print 'site_id', site_id, 'languagle', language, 'urlhash', urlhash
        print 'title', title, 'url', url, 'ext_content', ext_content
        print 'urls', filtered_urls
        try:
            db.insert_db(site_id, language, urlhash, title, url,
                         ext_content, html)
        except Exception, e:
            print e, type(url)
        try:
            map(db.submit_job, filtered_urls)
        except Exception, e:
            print e
        return (url, urlhash, status, domain, content)
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
    job = {"url": "http://tech.cnr.cn"}
    handle(json.dumps(job))
