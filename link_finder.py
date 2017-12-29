# Generic HTML parser to sift through website code
from html.parser import HTMLParser
from urllib import parse

# Take contents of parser and create a class with functions to be able to do more than what's available in the library 

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        # If tag is anchor tag -> check if attributes are href
        # For a tag, check the href and value
        # With the value, join it to the base url and add it to the set
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    # Return the set, to get all the links you need in the program
    def page_links(self):
        return self.links

    # If there's any errors, catch it and deliver the message
    def error(self, message):
        pass

# finder = LinkFinder()
# finder.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me</h1></body></html>')

