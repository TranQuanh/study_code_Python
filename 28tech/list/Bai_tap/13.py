m=10**9+7
n=int(input())
a=list(map(int,input().split()))
tong=0
tich=1
for x in a:
    tong+=x
    tong%=m
    tich*=x
    tich%=m
print(tong,tich)