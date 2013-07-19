#!/usr/bin/python
#coding=utf-8

import ssl
import urllib2
import httplib
import socket
import dns.resolver
import ConfigParser
import ast
import os

config = ConfigParser.RawConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'spider.cfg'))
#cfg = config.read('spider.cfg')

ns = ast.literal_eval(config.get('dns', 'nameservers'))


def resolve(host):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ns['nameservers']
    try:
        answer = resolver.query(host)
        return answer[0].address
    except dns.resolver.NXDOMAIN:
        return '127.0.0.1'


class CustomHTTPConnection(httplib.HTTPConnection):
    def connect(self):
        self.sock = socket.create_connection((
            resolve(self.host), self.port), self.timeout)


class CustomHTTPSConnection(httplib.HTTPSConnection):
    def connect(self):
        sock = socket.create_connection((
            resolve(self.host), self.port), self.timeout)
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file)


class CustomHTTPHandler(urllib2.HTTPHandler):
    def http_open(self, req):
        return self.do_open(CustomHTTPConnection, req)


class CustomHTTPSHandler(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(CustomHTTPSConnection, req)
