#!/usr/bin/env python
#coding=utf-8

import json
import redis
import config
import murmur
import MySQLdb
import cityhash
import tldextracter
from datetime import datetime

POOL = redis.ConnectionPool(host=config.RHOST,
                            port=config.RPORT,
                            db=config.RDB)


def init():
    '''
CREATE TABLE `jobs` (
`urlhash` BIGINT UNSIGNED PRIMARY KEY NOT NULL,
`domainhash` BIGINT UNSIGNED NOT NULL DEFAULT 0,
`type` TINYINT UNSIGNED DEFAULT 0 NOT NULL,
`frequency` TINYINT UNSIGNED DEFAULT 0 NOT NULL,
`fetched` TINYINT UNSIGNED DEFAULT 0 NOT NULL,
`processed` TINYINT UNSIGNED DEFAULT 0 NOT NULL,
`assigned_on` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
`fetched_on` TIMESTAMP DEFAULT '0000-00-00',
`status` SMALLINT UNSIGNED DEFAULT 408 NOT NULL,
`url` VARCHAR(512) NOT NULL DEFAULT ''
) Engine=INNoDB DEFAULT CHARSET=utf8;
    '''
    pass


def check_fetched(url):
    r = redis.Redis(connection_pool=POOL)
    mhash = murmur.string_hash(url)
    if r.getbit(config.BITMAP, mhash):
        return True
    else:
        r.setbit(config.BITMAP, mhash, 1)
        return False


def submit_job(url, detail=True):

    if isinstance(url, unicode):
        try:
            url = url.strip().encode('utf8')
        except Exception, e:
            print e
            pass
    if check_fetched(url):
        return False
    urlhash = cityhash.CityHash64(url)
    try:
        conn = MySQLdb.connect(host=config.QDB_HOST,
                               user=config.QDB_USER,
                               passwd=config.QDB_PASSWORD,
                               db=config.QDB_DB,
                               charset=config.QDB_CHARSET)
    except Exception, e:
        print e
        conn.close()
        return False
    cursor = conn.cursor()
    affected_rows = cursor.execute('select urlhash from jobs where urlhash'
                                   '= %s;', urlhash)
    if affected_rows:
        cursor.close()
        conn.close()
        return False
    else:
        r = redis.Redis(connection_pool=POOL)
        domain = tldextracter.extract_domain(url)
        if not domain:
            print 'domain is None'
            return False
        domainhash = cityhash.CityHash64(domain)
        cursor.execute('''insert into jobs(urlhash, domainhash, type, url) \
              values(%s, %s, %s, %s);''', (urlhash, domainhash, 1, url))
        conn.commit()
        rootdomain = tldextracter.extract_rootdomain(url)
        if not rootdomain:
            print 'rootdomain is None'
            return False
        job = {'url': url}
        if detail:
            r.rpush(config.QUEUE_FORMAT % rootdomain, json.dumps(job))
        else:
            r.lpush(config.QUEUE_FORMAT % rootdomain, json.dumps(job))
        cursor.close()
        conn.close()
        return True


def update_status(urlhash_status):
    urlhash, status = urlhash_status.split('|')
    try:
        conn = MySQLdb.connect(host=config.QDB_HOST,
                               user=config.QDB_USER,
                               passwd=config.QDB_PASSWORD,
                               db=config.QDB_DB,
                               charset=config.QDB_CHARSET)
    except Exception, e:
        print e
        conn.close()
        return False
    cursor = conn.cursor()
    affected_rows = cursor.execute('select * from jobs where urlhash = %s '
                                   'and fetched = 1;', (urlhash,))
    if affected_rows:
        cursor.close()
        conn.close()
        return False
    else:
        fetched_on = datetime.now()
        cursor.execute('update jobs set status=%s, fetched=1, fetched_on=%s'
                       'where urlhash=%s;', (status, fetched_on, urlhash))
        conn.commit()
        cursor.close()
        conn.close()
        return True


def get_jobs(limit=100):
    r = redis.Redis(connection_pool=POOL)
    queues = r.keys('queue_*')
    jobs = filter(None, [r.rpop(queue) for queue in queues])
    jobs = jobs + filter(None, [r.rpop(queue) for queue in queues])
    return jobs


def push(url, detail=True):

    if isinstance(url, unicode):
        try:
            url = url.strip().encode('utf8')
        except Exception, e:
            print e
            pass
    rootdomain = tldextracter.extract_rootdomain(url)
    if not rootdomain:
        return False
    if check_fetched(url):
        return False
    r = redis.Redis(connection_pool=POOL)
    job = {'url': url}
    if detail:
        r.rpush(config.QUEUE_FORMAT % rootdomain, json.dumps(job))
    else:
        r.lpush(config.QUEUE_FORMAT % rootdomain, json.dumps(job))
    return True


def insert_db(site_id, language, url_hash, title, url, content, html):

    try:
        conn = MySQLdb.connect(host=config.DB_HOST,
                               user=config.DB_USER,
                               passwd=config.DB_PASSWORD,
                               db=config.DB_DB,
                               charset=config.DB_CHARSET)
    except Exception, e:
        print e
        conn.close()
    cursor = conn.cursor()
    affected_rows = cursor.execute('select url_hash from news_site_html where'
                                   ' url_hash = %s;', url_hash)
    if affected_rows:
        cursor.close()
        conn.close()
        return False
    else:
        cursor.execute(
            'insert into news_site_html '
            '(site_id, language, url_hash, title, url, content, html) '
            'values(%s, %s, %s, %s, %s, %s, %s);',
            (site_id, language, url_hash, title, url, content, html))
        conn.commit()
        cursor.close()
        conn.close()
        return True


def get_site_info(domainhash):

    #site_info id domain_hash language name domain url
    try:
        conn = MySQLdb.connect(host=config.DB_HOST,
                               user=config.DB_USER,
                               passwd=config.DB_PASSWORD,
                               db=config.DB_DB,
                               charset=config.DB_CHARSET)
    except Exception, e:
        print e
        conn.close()

    cursor = conn.cursor()
    affected_rows = cursor.execute('select id, language from news_sites where'
                                   ' domainhash = %s;', domainhash)
    if affected_rows:
        result = cursor.fetchall()
        site_id, language = result[0]
        return (site_id, language)
    else:
        return (None, None)


if __name__ == '__main__':
    from rulers import RULERS
    urls = [RULERS[domain]["url"] for domain in RULERS]
    map(submit_job, urls)
