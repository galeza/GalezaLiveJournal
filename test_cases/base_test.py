'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''

import unittest
from common.config import driver_base
from page_objects.base_page import BasePage


class Basetest(unittest.TestCase):
    
        
    def setUp(self):
        dr = driver_base.DriverBase()
        BasePage.webdriver = dr.get_driver()  
        self.assertTrue(BasePage.webdriver != None, "Driver not set")      
        
    def tearDown(self):
        BasePage.webdriver.quit() 

