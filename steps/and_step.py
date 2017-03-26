'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''
from page_objects.rss_feed import RssFeed
from page_objects.top_feeds_page import TopFeedsPage
from page_objects.navigation.shop_menu import ShopMenu
from page_objects.shop_page import ShopPage
from wheel.signatures import assertTrue

class And(object):
    '''
    classdocs
    '''

    @staticmethod
    def user_tries_to_add_new_feed():
        RssFeed.add_new_feed()

    @staticmethod
    def user_browses_topfeeds_list():
        first_feed_desc = TopFeedsPage.get_feed_description()
        TopFeedsPage.browse_top_feed_list()
        second_feed_desc = TopFeedsPage.get_feed_description()
        assertTrue (first_feed_desc != second_feed_desc, "Feed was not changed")
    
    @staticmethod
    def user_clicks_upgrade_account_link():
        ShopMenu.click_link_upgrade()
        assertTrue (ShopPage.is_paid_features_displayed(), "Paid features not displayed")
        
    def __init__(self):
        '''
        Constructor
        '''
        