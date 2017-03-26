'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''
from base_test import Basetest
from steps.given import Given
from steps.and_step import And
from steps.then import Then


class RssFeedTests(Basetest):
    '''
    classdocs
    '''
    def test_user_can_not_add_new_feed_unless_login(self):
        Given.user_navigates_to_rss_page()
        And.user_tries_to_add_new_feed()
        Then.user_is_redirected_to_login_page()
        
    def test_user_can_browse_list_of_top_feeds(self):
        Given.user_navigates_to_top_feeds_page()
        And.user_browses_topfeeds_list()
        Then.user_navigates_back_to_rss_page()
        

if __name__ == '__main__':
    pass