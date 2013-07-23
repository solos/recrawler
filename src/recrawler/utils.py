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
from tldextracter import extract_domain
from tldextracter import extract_rootdomain
from htmlcontent import Extractor

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


def process(func):

    def wrapper(*args, **kwargs):
        url, urlhash, status, domain, content = func(*args, **kwargs)
        if not content:
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
