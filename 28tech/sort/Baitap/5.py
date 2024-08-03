
n=int(input())
a=list(map(int,input().split()))
a.sort()
dem=1
maxn=-10**9
so=a[0]
for i in range(1,n-1):
    if a[i]!=a[i+1]:
        if maxn<dem:
            maxn=dem
            so=a[i]
        dem=1
    else:
        dem+=1
if maxn<dem:
    maxn=dem
    i=a[-1]
print(so,maxn)