from math import isqrt
def snt(n):
    if n<2: return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

n=int(input())
a=list(map(int,input().split()))
b=[]
for x in a:
    if snt(x):b+=[x]
so=sum(b)/len(b)
print("%.3f"%so)
