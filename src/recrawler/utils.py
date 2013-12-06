#!/usr/bin/env python
#coding=utf-8

import re
import config
import magic
from rulers import RULERS


def generate_urls(filename):
    for line in file(filename):
        yield line.strip()


def check_mime(source):
    segment = source[:(len(source), 1024)[len(source) > 1024]]
    return magic.from_buffer(segment, mime=True) == 'text/html'


def url_filter(urls):
    pass


def url_clean(regex, urls):
    filtered_urls = []
    match = re.compile(regex)
    for _url in urls:
        _url = match.sub('', _url)
        filtered_urls.append(_url)
    filtered_urls = list(set(filtered_urls))
    return filtered_urls


def regex_filter(regex, urls):
    pattern = re.compile(regex)
    return filter(pattern.match, urls)


def ruler_filter(rootdomain, urls):
    filtered_urls = []
    for _url in urls:
        for prefix in RULERS[rootdomain]["rulers"]:
            if _url.startswith(prefix):
                filtered_urls.append(_url)
                break
    return filtered_urls


def suffix_filter(urls):
    filtered_urls = []
    for _url in urls:
        for suffix in config.IGNORE_SUFFIXES:
            if _url.endswith(suffix):
                continue
        filtered_urls.append(_url)
    return filtered_urls

if __name__ == '__main__':
    pass
