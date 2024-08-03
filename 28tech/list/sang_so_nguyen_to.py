from math import isqrt
m=10**6
Fibo = [True]*(m+1)
def sieve():
    Fibo[0]=Fibo[1]=False
    for i in range(2,isqrt(m)+1):
        if Fibo[i]:
            for j in range(i*i,m+1,i):
                Fibo[j]=False

sieve()
for i in range(100):
    if Fibo[i]:
        print(i,end=" ")