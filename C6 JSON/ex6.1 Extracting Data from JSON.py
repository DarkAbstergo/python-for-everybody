import json
import urllib.request, urllib.parse, urllib.error

name=input('Enter location:')
if len(name)<1: name='http://py4e-data.dr-chuck.net/comments_187450.json'
data=urllib.request.urlopen(name).read().decode()

info = json.loads(data)
info = info['comments']
tot=0
counts=0

for item in info:
    tot = tot + int(item['count'])
    counts = counts + 1

print('Retrieved', len(info),'characters')
print('Count:',counts)
print('Sum:',tot)

