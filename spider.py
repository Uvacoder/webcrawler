# Import module to connect to webpages directly from Python
from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *

# The spider will grab the link from the queue > Go to the page, grab the links from the HTML 
class Spider: 

    # Class variables (shared among all instances)
    # Declaring blank variables, therefore data can be passed on among them after
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    # It's faster to add data to a set than it is to a file
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)

    # Boot tells first spider what to do - create project directory > then two data files > and rest of spiders follow 

    @staticmethod
    def boot():
        # Refer to functions in the general.py file > Run functions for init spider to create relevant files and directory
        # Spider will the set the needed data the crawl
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
    
    # Function to tell spider to do the crawling and returns, how many pages in que + crawled

    @staticmethod
    def crawl_page(thread_name, page_url):
        # If page url isn't already crawled, then crawl it
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue: ' + str(len(Spider.queue)) + ' | Crawled: ' + str(len(Spider.crawled)))
            # Add the links not crawled into the queue, by gathering link
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            # Remove page being crawled from the queue and add it to the crawled file
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            # Update the files from the sets made
            Spider.update_files()

    # Simple stuff, convert HTML into readable code
    # If can't be converted, return an error and an empty set    
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try: 
            response = urlopen(page_url)
            # if response.getheader('Content-Type') == 'text/html':
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            # Feed the html content
            finder.feed(html_string)
        except:
            print("Error: Can't crawl the page!")
            return set()
        return finder.page_links()

    # After gathering links, add them to the queue

    @staticmethod
    def add_links_to_queue(links):
        # For every url in links, ensure that there it doesn't already exist
        for url in links:
            if url in Spider.queue:
                # Continue means to just pass over and ignore the url that's being checked
                continue
            if url in Spider.crawled:
                continue
            # You have to check domain name or else it will go on to other webpages
            # If domain name is not in url, continue
            if Spider.domain_name not in url:
                continue
            # Add the link to the queue if it pass all the test
            Spider.queue.add(url)
    
    # Update files using functions from general, and the sets that have been built

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)