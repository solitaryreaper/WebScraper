'''
Created on Sep 27, 2013

@author: excelsior
    
    Utility functions to export/import data in csv format
'''

import csv

def write_to_csv(csv_file, csv_data):
    writer = csv.writer(open(csv_file, 'wb') , delimiter='#')
    writer.writerows(csv_data)
    
if __name__ == '__main__':
    #celeb_data = []
    #sharukh_data = ['India', 'Actor', '1965']
    #amitabh_data = ['India', 'Actor', '1979']
    #write_to_csv("/tmp/healthyceleb.csv", celeb_data)
    test = "\u201cOm Shanti Om\u201d"
    print test.encode('utf8')