'''
Created on 25 mar 2017

@author: Dell Latitude E6530
'''

from base_test import Basetest
from steps.given import Given
from steps.and_step import And
from steps.then import Then


class ShopTests(Basetest):
    '''
    classdocs
    '''
    def test_user_cannot_upgrade_to_paid_account_unless_login(self):
        Given.user_navigates_to_shop_page()
        And.user_clicks_upgrade_account_link()
        Then.button_add_to_cart_is_disabled()
        
        
if __name__ == '__main__':
    pass