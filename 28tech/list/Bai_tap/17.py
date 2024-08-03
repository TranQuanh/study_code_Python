def check(a):
    l=0
    r=len(a)-1
    while l<=r:
        if a[l]!=a[r]: return False
        l+=1
        r-=1
    return True
n=int(input())
a=list(map(int,input().split()))
b=a[::-1]
if a==b:
    print("YES")
else:
    print("NO")
