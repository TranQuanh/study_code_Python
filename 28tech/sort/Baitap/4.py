from math import fabs
n=int(input())
a=list(map(int,input().split()))

a.sort()
minn=10**9
for i in range(1,n-1):
    minn = min(minn,fabs(a[i]-a[i+1]))
print(minn)        