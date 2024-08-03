from math import isqrt
def snt(n):
    for i in range(2,isqrt(n)+1):
        if n%i==0: return False
    return n>1  
n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    left=0
    for j in range(0,i):
        left+=a[j]
    right=0
    for j in range(i+1,n):
        right+=a[j]
    if snt(left) and snt(right):
        print(i)