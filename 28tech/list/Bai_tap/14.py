from math import gcd
n=int(input())
a=list(map(int,input().split()))
res=0
for x in a:
    res=gcd(res,x)