'''
Created on 20 mar 2017

@author: Dell Latitude E6530
'''
import json

class DriverConfigManager(object):
    '''
    classdocs
    '''

    full_config_dictionary = None

    def load_config(self):
        print "Loading tests configuration file" 
        if(self.full_config_dictionary == None):
            try:
                with open('../config.json') as config:    
                    self.full_config_dictionary = json.load(config)
            except IOError as e:
                print('Config file not found. Error code is:' + str(e.errno)) 
                       
    def get_browser(self):
        self.load_config()    
        return self.full_config_dictionary['browser']

    def get_url(self):
        self.load_config()      
        return self.full_config_dictionary['url']
    
    def __init__(self):
        '''
        Constructor
        '''
        