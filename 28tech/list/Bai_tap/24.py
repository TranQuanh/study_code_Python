n,k=map(int,input().split())
a=list(map(int,input().split()))
sum=0
for i in range(k):
    sum+=a[i]
print(sum,end=' ')
for i in range(k,n):
    sum= sum+a[i]-a[i-k]
    print(sum,end=' ')