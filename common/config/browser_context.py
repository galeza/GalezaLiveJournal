'''
Created on 26 mar 2017

@author: Dell Latitude E6530
'''

class BrowserConfig(object):
    '''
    classdocs
    '''
    
    browser_click_with_hoover = True
    
    @staticmethod
    def init_context(driver_config):
        browser = driver_config.get_browser().lower()
        if(browser == "firefox"):
            BrowserConfig.browser_click_with_hoover = False
        elif (browser == "chrome"):
            BrowserConfig.browser_click_with_hoover = True
        elif (browser == "ie"):
            BrowserConfig.browser_click_with_hoover = False
        else:
            BrowserConfig.browser_click_with_hoover = True
     
         

    def __init__(self, params):
        '''
        Constructor
        '''
        