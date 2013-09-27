'''
Created on Sep 27, 2013

@author: excelsior
    
    Utility functions to export/import data in csv format
'''

import csv

def write_to_csv(csv_file, csv_data):
    writer = csv.writer(open(csv_file, 'wb') , delimiter='#')
    writer.writerows(csv_data)
