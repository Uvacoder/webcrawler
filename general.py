# Allows you to create directories 
import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

# create_project_dir('mitul')    

# Only one URL given to the crawler
# The cue and files already crawled are needed
# Program can crawl multiple pages at once to improve speed
# Domain name without any ".com"

# Part 2 of Tutorial

# Create queue and crawled files (if not created)

def create_data_files(projectname, base_url):
    cue = projectname + '/cue.txt'
    crawled = projectname + '/crawled.txt'
    # When crawler starts, it will refer to the cue as to what to crawl
    # It can not be empty, because the crawler will have nothing to run

    # If cue file exists, don't create. vice versa
    if not os.path.isfile(cue):
        write_file(cue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Create a new file
# Opens path, writes data, closes file 
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()