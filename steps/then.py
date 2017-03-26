'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''
from wheel.signatures import assertTrue
from page_objects.login_page import Login
from page_objects.top_feeds_page import TopFeedsPage
from page_objects.rss_feed import RssFeed
from page_objects.shop_page import ShopPage

class Then(object):
    '''
    classdocs
    '''
    @staticmethod
    def user_is_redirected_to_login_page():
        assertTrue (Login.is_at_login_page(), "Login page not displayed")

    @staticmethod
    def user_navigates_back_to_rss_page():
        TopFeedsPage.navigate_back_to_rss_page()
        assertTrue (RssFeed.is_at_rss_feed_page(), "RSS page not displayed")
        
    @staticmethod
    def button_add_to_cart_is_disabled():
        assertTrue (ShopPage.is_btn_add_to_card_disabled(), "Button add to card is not disabled")
   
    def __init__(self, params):
        '''
        Constructor
        '''
        