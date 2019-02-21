import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
# or you can extract data from the duluth cinema webpage!:
# fhand=urllib.request.urlopen('http://www.marcustheatres.com/theatre-locations/duluth-cinema-duluth?Date=02-14-2019')
counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0)+1

lst=list()
for key,val in counts.items():
    lst.append((val,key))

lst=sorted(lst,reverse=True)
for val,key in lst[:5]:
    print(key,val)
