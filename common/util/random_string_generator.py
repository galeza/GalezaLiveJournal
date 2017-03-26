'''
Created on 23 mar 2017

@author: Dell Latitude E6530
'''
import random, string

class RandomStringGenerator(object):
    '''
    classdocs
    '''
    
    @staticmethod
    def random_string(length):
        return ''.join(random.choice(string.lowercase) for i in range(length))

    def __init__(self, params):
        '''
        Constructor
        '''
        