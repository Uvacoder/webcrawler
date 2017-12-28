# Generic HTML parser to sift through website code
from html.parser import HTMLParser
from urllib import parse

# Take contents of parser and create a class with functions to be able to do more than what's available in the library 

class LinkFinder(HTMLParser):

    def __init__(self):
        super().__init__()

    def handle_startendtag(self, tag, attrs):
        print(tag)

    # If there's any errors, catch it and deliver the message
    def error(self, message):
        pass

finder = LinkFinder()
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me</h1></body></html>')

