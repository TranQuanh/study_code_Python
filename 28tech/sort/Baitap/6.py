def binary_search(a,l,r,x):
    while l<=r:
        m=(l+r)//2
        if a[m]==x: return True
        elif a[m]>x: l=m+1
        elif a[m]<x:r=m-1
    return False
n=int(input())
a=list(map(int,input().split()))
for i in range(int(input())):
    t=int(input())
    print("YES" if binary_search(a,0,len(a)-1,t) else "NO")