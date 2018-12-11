import urllib, urllib, urllib
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = raw_input('Enter url: ')

uh = urllib.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)

commentsElement = tree.find('comments')
commentElements = commentsElement.findall('comment')

print(sum([int(comment.find('count').text) for comment in commentElements]))
    
    
