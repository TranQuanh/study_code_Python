n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a1=set(a)
b1=set(b)
c=a1.intersection(b1)
for x in a:
    if x in c:
        print(x,end=' ' )
        c.remove(x)
