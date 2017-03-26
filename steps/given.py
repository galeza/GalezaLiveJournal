'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''
from page_objects import main
from page_objects.navigation.header_menu import HeaderMenu 
from page_objects.rss_feed import RssFeed
from page_objects.shop_page import ShopPage
from page_objects.top_feeds_page import TopFeedsPage
from wheel.signatures import assertTrue

class Given(object):
    '''
    classdocs
    '''
    @staticmethod
    def user_is_at_main_page():
        assertTrue (main.Main.is_at_main_page(), "Main page not displayed")
 
    @staticmethod
    def user_is_at_rss_page():
        assertTrue (RssFeed.is_at_rss_feed_page(), "RSS page not displayed")

    @staticmethod
    def user_is_at_top_feed_page():
        assertTrue (TopFeedsPage.is_at_top_feed_page(), "Top Feeds page not displayed")

    @staticmethod
    def user_is_at_shop_page():
        assertTrue (ShopPage.is_at_shop_page(), "Shop page not displayed")
                               
    @staticmethod
    def user_navigates_to_rss_page():
        Given.user_is_at_main_page()
        HeaderMenu.click_btn_rss()
        Given.user_is_at_rss_page()
    
    @staticmethod
    def user_navigates_to_top_feeds_page():
        Given.user_navigates_to_rss_page()  
        RssFeed.open_top_feeds_page()

    @staticmethod        
    def user_navigates_to_shop_page():
        Given.user_is_at_main_page()
        HeaderMenu.click_btn_shop()
        Given.user_is_at_shop_page()
        
    @staticmethod        
    def user_navigates_to_help_page():
        Given.user_is_at_main_page()
        HeaderMenu.click_btn_help()         

    def __init__(self, params):
        '''
        Constructor
        '''
        