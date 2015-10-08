
# -*- coding:utf-8 -*-

import recrawler
import unittest
from recrawler.extracter import (extract_content,
                                 extract_links_by_regex,
                                 extract_links)
from mock import patch, MagicMock

import sys
sys.path.append('../src/')


class ExtracterTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch("recrawler.extracter.lxml.html.clean.Cleaner")
    def test_extract_content(self, mock_cleaner):
        mock_cleaner.return_value.clean_html.return_value = 'hulahoop'
        content = extract_content('hulahoop')
        self.assertEqual(content, 'hulahoop')

    def test_extract_links_by_regex(self):
        content = extract_links_by_regex(
            "www.google.com", "http://www.google.com")

    def test_extract_links(self):
        urls = extract_links('google.com', 'source')
        self.assertEqual(urls, [])


class UtilsTests(unittest.TestCase):

    def setUp(self):
        config = MagicMock(IGNORE_SUFFIXES=['com'])
        # def config_side_effect():
        #     return ['com']
        # config.IGNORE_SUFFIXES = config_side_effect()
        modules = {'config': config}
        self.module_patcher = patch.dict('sys.modules', modules)
        self.module_patcher.start()

    def test_url_clean(self):
        from recrawler import utils
        cleaned_url = utils.url_clean("http://www.", ["http://www.google.com"])
        self.assertEqual(cleaned_url, ["google.com"])

    def test_check_mime(self):
        from recrawler import utils
        input = '<!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">\r\n<html>\r\n <head>\r\n  <title>\r\n   Hello World Demonstration Document\r\n  </title>\r\n </head>\r\n <body>\r\n  <h1>\r\n   Hello, World!\r\n  </h1>\r\n  <p>\r\n   This is a minimal "hello world" HTML document. It demonstrates the\r\n   basic structure of an HTML file and anchors.\r\n  </p>\r\n  <p>\r\n   For more information, see the HTML Station at: <a href= \r\n   "http://www.december.com/html/">http://www.december.com/html/</a>\r\n  </p>\r\n  <hr>\r\n  <address>\r\n   &copy; <a href="http://www.december.com/john/">John December</a> (<a\r\n   href="mailto:john@december.com">john@december.com</a>) / 2001-04-06\r\n  </address>\r\n </body>\r\n</html>\r\n'
        mime = utils.check_mime(input)
        self.assertTrue(mime)

    def test_ruler_filter(self):
        from recrawler.utils import ruler_filter
        result = ruler_filter('arm.ac.uk',
                              ['http://www.arm.ac.uk/latest.htmlhttp://www.arm.ac.uk/press/'])
        self.assertEqual(result,
                         ['http://www.arm.ac.uk/latest.htmlhttp://www.arm.ac.uk/press/'])

    def test_suffix_filter(self):
        from recrawler.utils import suffix_filter
        result = suffix_filter(["http://www.hulahoop.org", "http://www.hulahoop.com"])
        self.assertEqual(result, ['http://www.hulahoop.org'])

    def test_url_clean(self):
        from recrawler.utils import url_clean
        result = url_clean("http://www.hulahoop.org", ["http://www.hulahoop.org", "http://www.hulahoop.com"])
        self.assertEqual(result, ['', 'http://www.hulahoop.com'])


class TLDExtracterTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_extract(self):
        from recrawler.tldextracter import extract
        result = extract("hulahoop.edu.au")
        self.assertEqual(result, ('', 'hulahoop.edu.au'))
        result_none = extract("hulahoop.xx.xx")
        map(self.assertIsNone, result_none)
        # self.assertIsNone(result_none)

    def test_extract_domain(self):
        from recrawler.tldextracter import extract_domain
        self.assertEqual('www.google.com',
                         extract_domain("http://www.google.com/hulahoop"))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultTestCase('test_version'))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite', verbosity=2)
