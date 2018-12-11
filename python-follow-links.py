# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib, urllib, urllib
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = raw_input('Enter html: ')
count = int(raw_input('Enter count: ')) - 1
repeat = int(raw_input('Enter repeat: '))

html = urllib.urlopen(url, context=ctx).read()

for i in range(0, repeat):
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    hrefs = [ tag.get('href', None) for tag in tags ]

    print(hrefs[count])

    html = urllib.urlopen(hrefs[count], context=ctx).read()
