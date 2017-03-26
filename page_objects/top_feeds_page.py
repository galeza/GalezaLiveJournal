'''
Created on 24 mar 2017

@author: Dell Latitude E6530
'''
from page_objects.locators import TopFeedsLocators
from page_objects.base_page import BasePage


class TopFeedsPage(object):
    '''
    classdocs
    '''

    @staticmethod
    def is_at_top_feed_page():
        return BasePage.is_displayed(TopFeedsLocators.TOP_FEEDS_LIST)
    
    @staticmethod
    def browse_top_feed_list():
        BasePage.wait_for_element_and_click(TopFeedsLocators.BROWSE_LINK)
        BasePage.wait_for_element_to_be_clickable(TopFeedsLocators.BROWSE_LINK)
     
    @staticmethod  
    def navigate_back_to_rss_page(): 
        BasePage.wait_for_element_and_click(TopFeedsLocators.BACK_TO_RSS_LINK)
    
    @staticmethod  
    def get_feed_description():
        BasePage.wait_element_present(TopFeedsLocators.TOP_FEEDS_LIST_ROW)
        row = BasePage.find(TopFeedsLocators.TOP_FEEDS_LIST_ROW)
        return row.text
               
    def __init__(self, params):
        '''
        Constructor
        '''
        