'''
Created on Sep 27, 2013

@author: excelsior
'''

from bs4 import BeautifulSoup

from utils import web_utils, csv_utils

# define constants here
EMPTY_STRING = ""

"""
    Get stats for a single celebrity using his/her URL from healthyceleb.com
"""

def get_stats_healthyceleb(url):
    print "Crawling URL .." + url
    html_content = web_utils.load_html_data_from_url(url)
    soup = BeautifulSoup(html_content)
    
    celeb_stats = {}
    # first extract the main div containing all the page content
    page_content = soup.find('div', {'class' : 'page-content'})
    
    # now extract the relevant children : 
    # <h3> represent attributes , <p> represents attribute values  
    children = page_content.findChildren()
    key, value = EMPTY_STRING, EMPTY_STRING
    for child in children:
        if child.name == "h3":
            key = child.string
        if child.name == "p" and key != EMPTY_STRING:
            value = child.string
            
            # Value would be NONE for complex tags which have multiple HTML elements
            if value is None:
                value = " ".join(child.stripped_strings)
                
            # Cleanup the extracted string
            value = value.strip()
            value = value.strip('\n')
            
            # If value is still empty, it implies probably the data is hidden in image
            if value is EMPTY_STRING:
                #print str(child)
                image = child.find('img')
                if image is not None:
                    value = image['alt']
                else:
                    value = "NA"
            
            celeb_stats[key] = value
            key, value = EMPTY_STRING, EMPTY_STRING
            
    return celeb_stats

"""
    Get the master list of all the URLs that need to be crawled for this site
"""    
def get_all_urls_celeb_stats(base_url):
    urls = []
    html_all_urls = web_utils.load_html_data_from_url(base_url)
    soup = BeautifulSoup(html_all_urls)
    
    all_urls = soup.findAll('loc')
    for url in all_urls:
        if "height-weight-body-statistics" in url.string:
            urls.append(url.string)
    return urls

if __name__ == '__main__':
    urls = get_all_urls_celeb_stats('http://healthyceleb.com/sitemap.xml')
    
    all_celeb_stats = []
    celeb_stats_file_header = []
    
    print "Starting crawl of all " + str(len(urls)) + " urls ..."
    for url in urls:
        try:
            celeb_stats = get_stats_healthyceleb(url)
            
            for field in celeb_stats.keys():
                celeb_stats_file_header.append(field)
            
            # collect the celeb stats
            all_celeb_stats.append(celeb_stats)
        except:
            print "Failed to crawl for URL : " + url
    print "Crawled all URLS .."
    
    all_unique_headers_set = set(celeb_stats_file_header)
    all_unique_headers = list(all_unique_headers_set)
    
    csv_all_celebs_data = []
    csv_all_celebs_data.append(all_unique_headers)
    print all_unique_headers
    
    for curr_celeb_stat in all_celeb_stats:
        csv_curr_celeb_data = []
        for field in all_unique_headers:
            if field in curr_celeb_stat:
                csv_curr_celeb_data.append(curr_celeb_stat[field])
            else:
                csv_curr_celeb_data.append("NA")
        
        csv_all_celebs_data.append(csv_curr_celeb_data)
        
    csv_utils.write_to_csv('/tmp/stats.csv', csv_all_celebs_data)
    print "Wrote data to CSV file .."

    
    
