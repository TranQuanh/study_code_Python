from sys import stdin
def check(n):
    r=n%10
    n//=10
    while n:
        c=n%10
        if c<r:return False
        r=c
        n//=10
    return True

d=dict({})
for line in stdin:
    a=list(map(int,line.split()))
    for x in a:
        if x in d:
            d[x]+=1
        else: d[x]=1
d=list(d.items())
d.sort(key=lambda x:[-x[1],x[0]])
for x,y in d:
    print(x,y)
