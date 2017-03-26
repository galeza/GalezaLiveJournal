'''
Created on 25 mar 2017

@author: Dell Latitude E6530
'''
from page_objects.base_page import BasePage
from page_objects.locators import ShopMenuLocators

class ShopMenu(object):
    '''
    classdocs
    '''

    @staticmethod
    def click_link_upgrade():
        BasePage.wait_for_element_and_click(ShopMenuLocators.UPGRADE_ACCOUNT_LINK)

    def __init__(self, params):
        '''
        Constructor
        '''
        