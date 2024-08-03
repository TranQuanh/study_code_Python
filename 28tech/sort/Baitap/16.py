def binary_search(a,l,r,x):
    while l<=r:
        m=(l+r)//2
        if a[m]==x:
            return True
        elif a[m]<x:
            l=m+1
        else:
            r=m-1
    return False
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
for i in range(0,n-1):
    if binary_search(a,0,n-1,a[i]+k):
        print("1")
        exit()
print("-1")