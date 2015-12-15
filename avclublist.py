# Description:
# Extract a list of books from the AV Club website
# Output as HTML with links to the books on Amazon.com
#
# Initial version: 12/14/2015
from bs4 import BeautifulSoup

import datetime
import urllib.request		# this for python 3 and later
import requests

amzSearch = '<a target="_blank" href="http://www.amazon.com/s/ref=as_li_ss_tl?_encoding=UTF8&camp=1789&creative=390957&field-keywords={0}&linkCode=ur2&tag=moss0e7-20&url=search-alias%3Daps&{1}</a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=moss0e7-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'

'''
amzSearch = '<a target="_blank" href="http://www.amazon.com/s/ref=as_li_ss_tl?_encoding=UTF8&camp=1789&creative=390957&field-keywords={0}&linkCode=ur2&tag=moss0e7-20&url=search-alias%3Daps&linkId=4JTWP2QOJSYBL7NU">{1}</a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=moss0e7-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'
'''

myURL = "http://www.avclub.com/article/our-favorite-graphic-novels-one-shots-and-archives-229423"
page = urllib.request.urlopen(myURL)

#parse
soup = BeautifulSoup(page, "html.parser")

# Extract all H4 items
rows = soup.find_all('h4')

#output
print('<html><head><title>Books to read</title></head><body><ul>')
for row in rows:
  print('<li>'+amzSearch+'</li>'.format(row.i, row.i))
print('</ul></body></html>')


