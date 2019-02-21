import re
numlist=list()
fh=open('regex_sum_187445.txt')
for line in fh:
    line=line.strip()
    extract=re.findall('([0-9]+)',line)
    if len(extract)<1: continue
    for i in range(len(extract)):
        num=float(extract[i])
        numlist.append(num)
print(numlist)
tot=0
count=0
for i in numlist:
    tot=tot+i
    count=count+1

print('total: ',tot,'average: ',tot/count)
