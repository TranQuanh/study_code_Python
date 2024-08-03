from math import fabs
n=int(input())
a=list(map(int,input().split()))
k=int(input())
min=10**18
for i in range(0,n):
    for j in range(i,n):
        if fabs(a[i]-a[j])<min:
            min=fabs(a[i]-a[j])
print(min)