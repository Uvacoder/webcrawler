# Import in url parser
from urllib.parse import urlparse

# Functions to extract the domain name and ensure it doesn't conflict w/ other sites

# Get the domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except: 
        return ''


# Get sub domain name (example.domain.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
