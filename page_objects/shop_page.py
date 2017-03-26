'''
Created on 25 mar 2017

@author: Dell Latitude E6530
'''
from page_objects.base_page import BasePage
from page_objects.locators import ShopLocators

class ShopPage(object):
    '''
    classdocs
    '''

    @staticmethod
    def is_at_shop_page():
        return BasePage.is_displayed(ShopLocators.PROMO_PAID_ACCOUNT)
      
    @staticmethod
    def is_paid_features_displayed():
        return BasePage.is_displayed(ShopLocators.PAID_FEATURES)
    
    @staticmethod
    def is_btn_add_to_card_disabled():
        BasePage.wait_element_present(ShopLocators.BTN_ADD_TO_CARD)
        btn = BasePage.find(ShopLocators.BTN_ADD_TO_CARD)
        return not btn.is_enabled()
        
    def __init__(self, params):
        '''
        Constructor
        '''
        