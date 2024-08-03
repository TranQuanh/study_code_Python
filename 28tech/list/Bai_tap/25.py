from sys import stdin

b=[]
for line in stdin:
    a=map(int,line.split())
    b.append(a)
chan,le=0,0
for x in b:
    if x%2==0: chan+=1
    else: le+=1
if chan<le:print("CHAN")
elif chan>le:print('LE')
else:print("CHANLE")