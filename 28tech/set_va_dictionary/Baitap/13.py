from math import isqrt
from os import stdin
def snt(n):
    for i in range(2,isqrt(n)+1):
        if n%i==0:return False
    return n>1
a=list(map(int,input().split()))

d=dict({})
for x in a:
    if snt(x):
        if x in d:
            d[x]+=1
        else:
            d[x]=1