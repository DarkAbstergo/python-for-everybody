import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
tot = 0
url = input("Enter a location: ")
if len(url)<1: url='http://py4e-data.dr-chuck.net/comments_187449.xml'
pg = urllib.request.urlopen(url)
data = pg.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for i in range(0,len(counts)):
    tot=tot+float(counts[i].text)
print('Retrieved',len(data),'characters')
print('Sum:', tot)

