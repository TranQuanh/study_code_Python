from math import isqrt
def snt(n):
    for i in range(2,isqrt(n)+1):
        if n%i==0: return False
    return n>1
a=[]
n=int(input())
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
dem=0
for i in range(n):
    if snt(a[i][i]):
        dem+=1
    if snt(a[i][n-1]): dem+=1
if n%2==1:
    if snt(a[n//2][n//2]):dem-=1
print(dem)
