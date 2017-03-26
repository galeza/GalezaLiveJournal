'''
Created on 23 mar 2017

@author: Dell Latitude E6530
'''
from page_objects.base_page import BasePage
from page_objects.locators import LoginLocators

class Login(object):
    '''
    classdocs
    '''
    @staticmethod
    def is_at_login_page():
        return BasePage.is_displayed(LoginLocators.LOGIN_FORM)


    def __init__(self, params):
        '''
        Constructor
        '''
        