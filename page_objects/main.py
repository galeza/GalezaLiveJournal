'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''
from page_objects.locators import MainLocators
from page_objects.base_page import BasePage
import time

class Main(BasePage):
    '''
    classdocs
    '''
    @staticmethod
    def is_at_main_page():
        time.sleep(5)    
        return BasePage.is_displayed(MainLocators.MAIN_H1)
    
    @staticmethod
    def is_promo_container_visible():
        return BasePage.is_displayed(MainLocators.PROMO_CONTAINER)

    def __init__(self, params):
        '''
        Constructor
        '''
        