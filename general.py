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

# Add data onto an existing file
# Call whenever you wanna add a new link into end of a file
def append_to_file(path, data):
    # Open path to file in append mode as file that you want to open 
    with open(path, 'a') as file: 
        file.write(data + '\n')


# Delete the contents of a file
# Get rid of everything within a file
def delete_file_contents(path):
    with open(path, 'w'):
        # Pass essentially means do nothing. This function writes "nothing" in the file.
        pass

# Store contents within a "Set" because a set can only have unique elements
# A page shouldn't be in both cue and crawled list

# Read a file and convert each line to set items
def file_to_set(file_name):
    # Create a variable for the set
    results = set()
    # Read text within a file, and for every line in that file
    # Add it to the set and replace the existing line break
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
        


# create_data_files('mitul', 'https://typicalmitul.com')



# 'a' means append. 'w' means write. 'rt' means read text file. '