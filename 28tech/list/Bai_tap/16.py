from math import isqrt
def snt(n):
    for i in range(2,isqrt(n)+1):
        if n%i==0: return False
    return n>1
def stn(n):
    sum=0
    so=n
    while n:
        sum=sum+n%10
        n//=10
    if sum==so: return True
    return False
def scp(n):
    so=isqrt(n)
    return so*so==n
def tongsnt(n):
    tong=0
    while(n):
        tong+=n%10
        n//=10
    return snt(tong)

n=int(input())
a=list(map(int,input().split()))
d1,d2,d3,d4=0,0,0,0
for x in a:
    if snt(x): d1+=1
    if stn(x):d2+=1
    if scp(x):d3+=1
    if tongsnt(x):d4+=1
print(d1,d2,d3,d4,sep='\n')

        
        