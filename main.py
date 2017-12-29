# Each thread works on it's own job from the queue
import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

# Setting the project name and content to be crawled
# It is in caps lock because it will stay constant throughout the document

PROJECT_NAME = 'citc-links'
HOMEPAGE = 'http://www.citc.ai/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
# Number 
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create worker threads (will end when main exists)
# If you want to terminate program, it will terminate spiders as well
def create_workers():
    # Creating 8 generic threads
    # Use an "_", if you don't need to use the variable later
    for _ in range(NUMBER_OF_THREADS):
        # Defines what the thread will do AND can only do one thing
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Function for the actual work that has to be done
# Do the next job in the queue 
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        # It tells computer that everything is done 
        queue.task_done()

# Each queued link is a new job 
def create_jobs():
    # For every link within the file
    # "Put" the link into the queue
    # Join it so that the spiders don't interfere with each other
    # Repeat until queue is empty
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# Check if there are items in the queue, if so - crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    # If there is links qued, then tell which files and run create jobs
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links are in queue.')
        create_jobs()

create_workers()
crawl()