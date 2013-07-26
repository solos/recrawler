#!/usr/bin/env python
#coding=utf-8

import json
import redis
import config
import cityhash
import PySQLPool
import tldextracter
from datetime import datetime

POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

queueconnection = PySQLPool.getNewConnection(
    username=config.QDB_USER,
    password=config.QDB_PASSWORD,
    host=config.QDB_HOST,
    db=config.QDB_DB,
    charset=config.QDB_CHARSET)

connection = PySQLPool.getNewConnection(
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    db=config.DB_DB,
    charset=config.DB_CHARSET)


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


def submit_job(url, detail=True):

    if isinstance(url, unicode):
        try:
            url = url.strip().encode('utf8')
        except Exception, e:
            print e
            pass
    urlhash = cityhash.CityHash64(url)
    query = PySQLPool.getNewQuery(queueconnection)
    query.Query('''select urlhash from jobs where urlhash = %s;''', urlhash)
    if query.record:
        return False
    else:
        r = redis.Redis(connection_pool=POOL)
        domain = tldextracter.extract_domain(url)
        domainhash = cityhash.CityHash64(domain)
        query.Query('''insert into jobs(urlhash, domainhash, type, url) \
              values(%s, %s, %s, %s);''', (urlhash, domainhash, 1, url))
        query.Pool.Commit()
        rootdomain = tldextracter.extract_rootdomain(url)
        if not rootdomain:
            return False
        job = {'url': url}
        if detail:
            r.rpush(config.QUEUE_FORMAT % rootdomain, json.dumps(job))
        else:
            r.lpush(config.QUEUE_FORMAT % rootdomain, json.dumps(job))
        return True


def update_status(urlhash_status):
    urlhash, status = urlhash_status.split('|')
    query = PySQLPool.getNewQuery(queueconnection)
    query.Query('''select * from jobs where urlhash = %s and fetched = 1;''',
                (urlhash,))
    if query.record:
        return False
    else:
        fetched_on = datetime.now()
        query.Query('update jobs set status=%s, fetched=1, fetched_on=%s'
                    'where urlhash=%s;', (status, fetched_on, urlhash))
        query.Pool.Commit()
        return True


def get_jobs(limit=100):
    r = redis.Redis(connection_pool=POOL)
    jobs = filter(None, [r.rpop(queue) for queue in config.QUEUES])
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
    r = redis.Redis(connection_pool=POOL)
    job = {'url': url}
    if detail:
        r.rpush(config.QUEUE_FORMAT % rootdomain, json.dumps(job))
    else:
        r.lpush(config.QUEUE_FORMAT % rootdomain, json.dumps(job))
    return True


if __name__ == '__main__':
    sites = json.loads(open('sites.json', 'r').read())
    urls = [site['url'] for site in sites]
    map(submit_job, urls)
    #pass
    #domainhash = 1475423385534659117
    #print get_site_info(domainhash)
