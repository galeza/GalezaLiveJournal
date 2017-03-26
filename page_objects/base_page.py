'''
Created on 22 mar 2017

@author: Dell Latitude E6530
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    '''
    classdocs
    '''
    webdriver = None
        
    @staticmethod
    def is_displayed(locator):
        try:
            BasePage.wait_element_present(locator)
            return BasePage.find(locator).is_displayed()
        except:
            return False
        
    @staticmethod
    def are_displayed(locator):
        try:
            BasePage.wait_elements_present(locator)
            result = False
            elements = BasePage.finds(locator)
            for element in elements:
                result = result and element.is_displayed()          
            return result
        except:
            return False

    
    @staticmethod
    def find(locator):
        return BasePage.webdriver.find_element(*locator)
    
    @staticmethod
    def finds(locator):
        return BasePage.webdriver.find_elements(*locator)
     
    @staticmethod
    def find_elements(web_element, tag):
        return web_element.find_elements(tag)
    
    @staticmethod
    def wait_element_present(locator):
        wait = WebDriverWait(BasePage.webdriver, 10)
        wait.until(EC.presence_of_element_located(locator))
        
    @staticmethod
    def wait_elements_present(locator):
        wait = WebDriverWait(BasePage.webdriver, 10)
        wait.until(EC.presence_of_all_elements_located(locator))
          
    @staticmethod
    def wait_for_element_and_click(locator):
        BasePage. wait_for_element_to_be_clickable(locator)
        BasePage.find(locator).click()
        
    @staticmethod
    def wait_for_elements_and_click(locator, index):
        elements = BasePage.finds(locator)
        #element = elements[index] 
        elements[index].is_displayed()
        elements[index].click()

    @staticmethod
    def wait_for_element_to_be_clickable(locator):
        wait = WebDriverWait(BasePage.webdriver, 10)
        wait.until(EC.element_to_be_clickable(locator))   
 
    @staticmethod
    def wait_for_visibility_of_element(locator):
        wait = WebDriverWait(BasePage.webdriver, 10)
        wait.until(EC.visibility_of_element_located(locator))   
                   
    def __init__(self, params):
        '''
        Constructor
        '''
        