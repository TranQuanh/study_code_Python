def bin1(a,l,r,x):
    res=-1
    while l<=r:
        m=(l+r)//2
        if a[m]==x:
            res = m
            r=m-1
        elif a[m]<x:
            l=m+1
        else:
            r=m-1
    return res
def bin2(a,l,r,x):
    res=-1
    while l<=r:
        m=(l+r)//2
        if a[m]==x:
            res = m
            l=m+1   
        elif a[m]<x:
            l=m+1
        else:
            r=m-1
    return res
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
dem=0
for i in range(0,n-1):
    so1=bin1(a,i+1,n-1,k-a[i])
    so2=bin2(a,i+1,n-1,k-a[i])
    if so1!=-1:
        dem+=so2-so1+1
print(dem)