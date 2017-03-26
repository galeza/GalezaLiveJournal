'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''

class Locators(object):
    '''
    classdocs
    '''
from selenium.webdriver.common.by import By

class HeaderMenuLocators(object):
    
    """A class for Header Menu locators. All Header Menu locators should come here"""
    HEADER_MENU_XPATH = "//div[@class='s-header__nav']"
    BTN_FIND_MORE = (By.XPATH, HEADER_MENU_XPATH + "/ul/li")
    BTN_SHOP = (By.XPATH, HEADER_MENU_XPATH + "/ul/li[2]")
    BTN_HELP = (By.XPATH, HEADER_MENU_XPATH + "/ul/li[3]")
    BTN_COMMUNITIES = (By.XPATH, HEADER_MENU_XPATH + "//ul/li/ul/li[1]")
    BTN_RSS = (By.XPATH, HEADER_MENU_XPATH + "/ul/li/ul/li[2]")

class MainLocators(object):
    
    """A class for Main page locators. All Main page locators should come here"""
    MAIN_H1 = (By.CSS_SELECTOR, "h1.b-mainpage-intro-heads")
    PROMO_CONTAINER = (By.CSS_SELECTOR, "div.b-ljpromo-container")
    
class RssLocators(object):
    
    """A class for Rss page locators. All Rss page locators should come here"""
    RSS_H3 = (By.CSS_SELECTOR, "h3.synpage-add__title")
    RSS_ADD_NOTE = (By.CSS_SELECTOR, "small.synpage-add__note")
    RSS_ADD_FEED_URL = (By.NAME, "synurl")
    RSS_SUBMIT_BUTTON = (By.NAME, "action:addcustom")
    TOP_FEEDS_LINK = (By.CSS_SELECTOR, "a[href='http://www.livejournal.com/syn/list.bml']")

class LoginLocators(object):
    
    """A class for Login page locators. All Login page locators should come here"""
    LOGIN_FORM = (By.XPATH, "(//input[@id='user'])[2]")

class TopFeedsLocators(object):
    
    """A class for Top Feeds page locators. All Top Feeds page locators should come here"""
    TOP_FEEDS_LIST = (By.XPATH, "//table[contains(@class,'synpage-section__items')]")
    BROWSE_LINK = (By.CSS_SELECTOR, "a[href='/syn/list.bml?page=3']")
    BACK_TO_RSS_LINK = (By.CSS_SELECTOR, "a[href='/syn/']")
    TOP_FEEDS_LIST_ROW = (By.XPATH, "//table[contains(@class,'synpage-section__items')]/tbody/tr[2]/td[3]/a")
    

class ShopLocators(object):
    
    """A class for Shop page locators. All Shop page locators should come here"""
    PROMO_PAID_ACCOUNT = (By.CSS_SELECTOR, "a[href='/shop/paidaccount.bml']")
    PAID_FEATURES = (By.CSS_SELECTOR, "div.b-paidfeatures")
    BTN_ADD_TO_CARD = (By.CSS_SELECTOR, "button.canyon-side")
    

class ShopMenuLocators(object):
    """A class for Shop Menu locators. All Shop Menu locators should come here"""
    UPGRADE_ACCOUNT_LINK = (By.PARTIAL_LINK_TEXT, "Upgrade to a Paid Account")
          
    def __init__(self, params):
        '''
        Constructor
        '''
        