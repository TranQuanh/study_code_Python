from math import fabs
n=int(input())
a=list(map(int,input().split()))
a.sort(key=fabs)
print(a)