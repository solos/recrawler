#!/usr/bin/env python
#coding=utf-8

import re
import lxml.html
import lxml.html.clean


cleaner = lxml.html.clean.Cleaner(
    scripts=True,
    javascript=True,
    comments=True,
    style=True,
    links=True,
    meta=True,
    page_structure=True,
    processing_instructions=True,
    embedded=True,
    frames=True,
    forms=True,
    annoying_tags=True,
    remove_tags=None,
    allow_tags=None,
    kill_tags=None,
    remove_unknown_tags=True,
    safe_attrs_only=True,
    safe_attrs=frozenset(['abbr', 'accept', 'accept-charset']),
    add_nofollow=False,
    host_whitelist=(),
    whitelist_tags=set(['embed', 'iframe']),
    _tag_link_attrs={'a': 'href', 'applet': ['code', 'object']})


def extract_links(url, source, xpath='//a[@href]'):
    urls = []
    if not source or not isinstance(source, unicode):
        return urls
    if isinstance(url, unicode):
        url = url.encode('utf8')
    try:
        absolute_content = lxml.html.make_links_absolute(source, url)
        tree = lxml.html.fromstring(absolute_content)
    except Exception, e:
        print e
        return urls
    #extract links
    elems = tree.xpath(xpath)
    urls = map(lambda a: a.attrib['href'], elems)
    return list(set(urls))


def extract_links_by_regex(url, source, regex='''(?P<url>http://.*?)["']'''):
    pattern = re.compile(regex)
    return list(set(pattern.findall(source)))


def extract_content(url, source):

    cleaned = cleaner.clean_html(source)
    content = lxml.html.fromstring(cleaned).text_content()
    return content


def extract_data(url, source, xpath):
    pass


def extract_data_by_xpath(url, source, xpath):
    pass


def extract_data_by_regex(url, source, regex):
    pass


if __name__ == '__main__':
    import fetcher
    url = 'http://www.baidu.com'
    status, content = fetcher.fetch(url)
    _, ucontent = encoding.html_to_unicode('', content)
    print extract_links(url, ucontent)
    print extract_content(url, ucontent)
