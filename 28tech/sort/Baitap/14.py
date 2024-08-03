def bin(a,l,r,x):
    res=-1
    while l<=r:
        m=(l+r)//2
        if a[m]>x:
            res=m
            r=m-1
        else:
            l=m+1
    return res
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
dem=0
for i in range(0,n-1):
    so1=bin(a,i+1,n-1,k-a[i])
    if so1!=-1:
        dem+=n-so1
print(dem)