def stn(n):
    tmp=n
    tong=0
    while n:
        tong=tong*10+n%10
        n//=10
    return tong == tmp
a=[]
n=int(input())
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
dem=0
for i in range(n):
    for j in range(0,i+1):
        if stn(a[i][j]):dem+=1