n,m=map(int,input().split())
a=list(map(int,input().split()))
l,r=0,n-1
dem=0
while l<=r:
    if a[l]+a[r]<=m:
        dem+=1
        l+=1
        r-=1
    else:
        dem+=1
        r-=1
print(dem)
