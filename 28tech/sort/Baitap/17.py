n,p=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
maxn=max(a[0],p-a[-1])
for i in range(1,n-1):
    maxn=max(maxn,(a[i]-a[i-1])/2)
print(maxn)