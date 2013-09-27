'''
Created on Sep 27, 2013

@author: excelsior
    
    Utility functions to fetch data from web
'''

import urllib2

'''
    Loads HTML text of a webpage whose URL is provided
'''
def load_html_data_from_url(url):
    return urllib2.urlopen(url).read()
