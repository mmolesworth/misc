import json
import urllib
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = raw_input('Enter url: ')

uh = urllib.urlopen(url, context=ctx)

data = uh.read()

info = json.loads(data)
comments = info['comments']

# for comment in comments:
#   print(comment['count'])

print(sum([int(comment['count']) for comment in comments]))
