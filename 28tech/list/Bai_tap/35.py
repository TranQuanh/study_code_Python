from math import isqrt
m=10**6
F=[True]*(m+1)
def init():
    F[0]=F[1]=False
    for i in range(2,isqrt(m)+1):
        if F[i]:
            for j in range(i*i,m+1,i):
                F[j]=False     

init()
fibo=[0]*(10**6+1)
fibo[0]=0
fibo[1]=0
sum=0
for i in range(2,10**6+1):
    if F[i]:
        sum+=1
    fibo[i]=sum
for i in range(int(input())):
    l,r=map(int,input().split())
    if l==0:print(fibo[r])
    else: print(fibo[r]-fibo[l])
            
                