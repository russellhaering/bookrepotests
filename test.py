import unittest
import re
from urllib import urlencode
from urllib2 import urlopen

class TestBookSearch(unittest.TestCase):
        def setUp(self):
            self.url = "http://www.mattcorley.biz/onlinebookrepos/searchresults.php"

        def testTitleHasResults(self):
            data = urlencode({
                'title': 'Criminal',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("1234567890123", text))

        def testTitleHasNoResults(self):
            data = urlencode({
                'title': 'Mastermind',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("No results were found", text))

        def testFullISBNHasResults(self):
            data = urlencode({
                'isbn': '1234567890123',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("Criminal", text))

        def testFullISBNHasNoResults(self):
            data = urlencode({
                'title': '3210987654321',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("No results were found", text))

        def testAuthorPartialHasResults(self):
            data = urlencode({
                'authorName': 'James',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("1234567890123", text))

        def testAuthorPartialHasNoReults(self):
            data = urlencode({
                'authorName': 'Orwell',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("No results were found", text))

        def testKeywordHasResults(self):
            data = urlencode({
                'keyword': 'First',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("0000000000001", text))

        def testKeywordHasNoResults(self):
            data = urlencode({
                'keyword': 'Last',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("No results were found", text))

        def testAuthorKeywordHasResults(self):
            data = urlencode({
                'keyword': 'exploits',
                'authorName': 'James',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("1234567890123", text))

        def testAuthorTitleHasResults(self):
            data = urlencode({
                'title': 'Criminal',
                'authorName': 'James',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("1234567890123", text))

        def testAuthorISBNHasResults(self):
            data = urlencode({
                'isbn': '1234567890123',
                'authorName': 'James',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("1234567890123", text))

        def testAllHasResults(self):
            data = urlencode({
                'title': 'Criminal',
                'isbn': '1234567890123',
                'authorName': 'James',
                'keyword': 'exploits',
            })
            handle = urlopen(self.url, data)
            text = handle.read()
            self.assertTrue(re.search("1234567890123", text))
