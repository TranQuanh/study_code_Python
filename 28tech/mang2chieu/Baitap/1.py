from math import isqrt
def snt(n):
    for i in range(2,isqrt(n)+1):
        if n%i==0:return False
    return n>1
a=[]
n,m=map(int,input().split())
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
for i in range(n):
    for j in range(m):
        if snt(a[i][j]):
            print(a[i][j],end=' ')
    print()