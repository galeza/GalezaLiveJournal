'''
Created on 25 mar 2017

@author: Dell Latitude E6530
'''
import unittest
from test_cases.rss_feed_tests import RssFeedTests
from test_cases.shop_tests import ShopTests
 
# get all tests
rss_feed = unittest.TestLoader().loadTestsFromTestCase(RssFeedTests)
shop = unittest.TestLoader().loadTestsFromTestCase(ShopTests)
 
# create a test suite combining rss tests and shop test
test_suite = unittest.TestSuite([rss_feed, shop])
 
# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)