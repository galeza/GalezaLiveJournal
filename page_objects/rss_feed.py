'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''
from page_objects.locators import RssLocators
from page_objects.base_page import BasePage
from common.util.random_string_generator import RandomStringGenerator


class RssFeed (object):
    '''
    classdocs
    '''
    @staticmethod
    def is_at_rss_feed_page():
        return BasePage.is_displayed(RssLocators.RSS_H3)

    @staticmethod
    def get_note_info():
        featureNoteElement = BasePage.find(RssLocators.RSS_ADD_NOTE)
        return featureNoteElement.text
    
    @staticmethod   
    def add_new_feed():
        new_feed = BasePage.find(RssLocators.RSS_ADD_FEED_URL)
        new_feed.send_keys(RandomStringGenerator.random_string(5))
        BasePage.wait_for_element_and_click(RssLocators.RSS_SUBMIT_BUTTON)
    
    @staticmethod   
    def open_top_feeds_page():
        BasePage.is_displayed(RssLocators.TOP_FEEDS_LINK)
        BasePage.find(RssLocators.TOP_FEEDS_LINK).click()
        
    
    
    def __init__(self, params):
        '''
        Constructor
        '''
        