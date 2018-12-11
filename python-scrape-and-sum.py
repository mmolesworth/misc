from urllib import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = raw_input('Enter - ')
print(url)
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup.findAll("span", {"class" : "comments"})

x = sum([int(tag.contents[0]) for tag in tags ])

print(x)
