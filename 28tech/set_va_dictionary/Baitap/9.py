n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a1=set(a)
b1=set(b)
c=list(a1.difference(b1))
c.sort()
for x in c:
    print(x,end=' ')

