def bin1(a,l,r,x):
    res=-1
    while l<=r:
        m=(l+r)//2
        if a[m]==x:
            res=m
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
            res=m
            l=m+1
        elif a[m]<x:
            l=m+1
        else:
            r=m-1
    return res
def bin3(a,l,r,x):
    res=-1
    while l<=r:
        m =(l+r)//2
        if a[m]>=x:
           res=m
           r=m-1
        else:
            l=m+1   
    return res
def bin4(a,l,r,x):
    res=-1
    while l<=r:
        m =(l+r)//2
        if a[m]>x:
           res=m
           r=m-1
        else:
            l=m+1   
    return res
def bin5(a,l,r,x):
    so1=bin1(a,l,r,x)
    so2=bin2(a,l,r,x)
    if so1 != (-1):
        return so2-so1+1
    else:
        return 0

n,x =map(int,input().split())
a=list(map(int,input().split()))
h1,h2,h3,h4,h5=bin1(a,0,n-1,x),bin2(a,0,n-1,x),bin3(a,0,n-1,x),bin4(a,0,n-1,x),bin5(a,0,n-1,x)
print(h1,h2,h3,h4,h5,sep="\n")