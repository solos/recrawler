#!/usr/bin/env python
#coding=utf-8

import re
import urlnorm
import encoding
import lxml.html
import lxml.html.clean


url_match = re.compile(r'#.*$', re.DOTALL)

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


def extract_links(url, source):
    filtered_urls = []
    if not source or not isinstance(source, unicode):
        print 'not unicode'
        return filtered_urls
    if isinstance(url, unicode):
        url = url.encode('utf8')
    try:
        absolute_content = lxml.html.make_links_absolute(source, url)
        tree = lxml.html.fromstring(absolute_content)
    except Exception, e:
        print e
        return filtered_urls

    #extract links
    elems = tree.xpath('//a[@href]')
    urls = map(lambda a: a.attrib['href'], elems)
    urls = list(set(urls))
    for _url in urls:
        _url = url_match.sub('', _url)
        try:
            _url = urlnorm.norm(_url)
        except Exception, e:
            print e
            continue
        filtered_urls.append(_url)
    filtered_urls = list(set(filtered_urls))
    return filtered_urls


def extract_content(url, source):

    cleaned = cleaner.clean_html(source)
    content = lxml.html.fromstring(cleaned).text_content()
    return content


def extract_data(url, source):
    pass


if __name__ == '__main__':
    import fetcher
    url = 'http://www.baidu.com'
    status, content = fetcher.fetch(url)
    _, ucontent = encoding.html_to_unicode('', content)
    print extract_links(url, ucontent)
    print extract_content(url, ucontent)
