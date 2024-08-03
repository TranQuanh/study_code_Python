n,k=map(int,input().split())
a=list(map(int,input().split()))
a[1:].sort(reverse=True)
tong=0
for i in range(0,k+1):
    tong+=a[i]
for i in range(k+1,n):
    tong-=a[i]
print(tong)
    