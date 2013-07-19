#!/usr/bin/python
#coding=utf-8

import urllib2
import random
import cookielib

from gziphandler import GzipHandler
import ConfigParser
from proxy import PROXYS
from useragent import USER_AGENTS

config = ConfigParser.RawConfigParser()
config.read('spider.cfg')

#cookie support
CookieHandler = urllib2.HTTPCookieProcessor(cookielib.CookieJar())

#auth
AuthHandler = urllib2.HTTPBasicAuthHandler()
AuthHandler.add_password(
    realm='PDQ Application',
    uri='https://mahler:8092/site-updates.py',
    user='klem',
    passwd='kadidd!ehopper')


def get_proxy_opener():
    proxy_index = random.randint(0, len(PROXYS)-1)
    ProxyHandler = urllib2.ProxyHandler(PROXYS[proxy_index])
    proxy_opener = urllib2.build_opener(
        GzipHandler,
        ProxyHandler,
        CookieHandler,
    )
    user_agent_index = random.randint(0, len(USER_AGENTS)-1)
    user_agent = USER_AGENTS[user_agent_index]
    proxy_opener.addheaders = [
        ('user-agent', user_agent),
        ('connection', 'keep-alive')]
    return proxy_opener


def get_opener():
    opener = urllib2.build_opener(
        GzipHandler,
        CookieHandler,
    )
    user_agent_index = random.randint(0, len(USER_AGENTS)-1)
    user_agent = USER_AGENTS[user_agent_index]
    opener.addheaders = [
        ('user-agent', user_agent),
        ('connection', 'keep-alive')]
    return opener


def test_proxy():
    pass
    #proxy_opener.addheaders = [(
#    'User-agent',
#    '''curl/7.22.0 (x86_64-pc-linux-gnu) libcurl/7.22.0 OpenSSL/1.0.1 '''
#    '''zlib/1.2.3.4 libidn/1.23 librtmp/2.3''')]
#urllib2.install_opener(opener)
