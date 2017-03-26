'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''
from page_objects.locators import HeaderMenuLocators
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base_page import BasePage
from wheel.signatures import assertTrue
from common.config.browser_context import BrowserConfig
import time

class HeaderMenu(BasePage):
    '''
    classdocs
    '''

    @staticmethod
    def is_findmore_button_visible():
        return BasePage.is_displayed(HeaderMenuLocators.BTN_FIND_MORE)
    
    @staticmethod
    def is_rss_button_visible():
        return BasePage.is_displayed(HeaderMenuLocators.BTN_RSS)
    
    @staticmethod
    def is_communities_button_visible():
        return BasePage.is_displayed(HeaderMenuLocators.BTN_COMMUNITIES)
    
    @staticmethod
    def is_shop_button_visible():
        return BasePage.is_displayed(HeaderMenuLocators.BTN_SHOP)
    
    @staticmethod
    def is_help_button_visible():
        return BasePage.is_displayed(HeaderMenuLocators.BTN_HELP)
    
    @staticmethod
    def click_btn_findmore():
        assertTrue (HeaderMenu.is_findmore_button_visible(), "Find more button not displayed")
        BasePage.find(HeaderMenuLocators.BTN_FIND_MORE).click()
        
    @staticmethod
    def click_btn_shop():
        assertTrue (HeaderMenu.is_shop_button_visible(), "Shop button not displayed")
        BasePage.find(HeaderMenuLocators.BTN_SHOP).click()
        
    @staticmethod
    def click_btn_help():
        assertTrue (HeaderMenu.is_help_button_visible(), "Help button not displayed")
        BasePage.find(HeaderMenuLocators.BTN_HELP).click()
        
    @staticmethod
    def click_btn_rss():
        if(BrowserConfig.browser_click_with_hoover == False):
            #firefox
            BasePage.wait_element_present(HeaderMenuLocators.BTN_FIND_MORE)
            assertTrue (HeaderMenu.is_findmore_button_visible(), "Find more button not displayed")
            BasePage.find(HeaderMenuLocators.BTN_FIND_MORE).click()
            BasePage.wait_for_visibility_of_element(HeaderMenuLocators.BTN_RSS)
            BasePage.find(HeaderMenuLocators.BTN_RSS).click()
        else:   
            #chrome
            assertTrue (HeaderMenu.is_findmore_button_visible(), "Find more button not displayed")
            buttonFindMore = BasePage.find(HeaderMenuLocators.BTN_FIND_MORE)
            actions = ActionChains(BasePage.webdriver)
            actions.move_to_element(buttonFindMore).perform()
            time.sleep(1)
            assertTrue (HeaderMenu.is_rss_button_visible(), "RSS button not displayed")
            buttonRss = BasePage.find(HeaderMenuLocators.BTN_RSS)
            actions.move_to_element(buttonRss)
            actions.click(buttonRss).perform()
         
        
    @staticmethod
    def click_btn_communities():
        assertTrue (HeaderMenu.is_findmore_button_visible(), "Find more button not displayed")
        buttonFindMore = BasePage.find(HeaderMenuLocators.BTN_FIND_MORE)
        actions = ActionChains(BasePage.webdriver)
        actions.move_to_element(buttonFindMore).perform()
        time.sleep(1)
        assertTrue (HeaderMenu.is_communities_button_visible(), "Communities button not displayed")
        buttonCom = BasePage.find(HeaderMenuLocators.BTN_COMMUNITIES)
        actions.move_to_element(buttonCom)
        actions.click(buttonCom).perform()

        

    def __init__(self, params):
        '''
        Constructor
        '''
        