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
s=set({})
for i in range(n):
    if snt(a[i][i]):
        s.add(a[i][i])
    if snt(a[i][n-i-1]): 
        s.add(a[i][n-i-1])
print(len(s))
