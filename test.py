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

        def testPartialISBNHasResults(self):
            data = urlencode({
                'isbn': '12345',
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
