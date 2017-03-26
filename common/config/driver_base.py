'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''
from selenium import webdriver
from common.config.driver_config_manager import DriverConfigManager
from common.config.browser_context import BrowserConfig


class DriverBase(object):
    '''
    classdocs
    '''
    
    def get_driver(self):
        driver_config = DriverConfigManager()
        driver = None
        browser = driver_config.get_browser().lower()
        if(browser == "firefox"):
            driver = self.get_firefox_driver()
        elif (browser == "chrome"):
            driver = self.get_chrome_driver()
        elif (browser == "ie"):
            driver = self.get_ie_driver()
        else:
            driver = self.get_firefox_driver()
        BrowserConfig.init_context(driver_config)       
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(driver_config.get_url())
        return driver

    def get_chrome_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--lang=en')
        driver = webdriver.Chrome(chrome_options=options) 
        return driver
    
    def get_firefox_driver(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages','en')
        #profile.native_events_enabled = False
        driver = webdriver.Firefox(profile)
        return driver

    def get_ie_driver(self):
        return webdriver.Ie()
    
    def __init__(self):
        '''
        Constructor
        '''
        