m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
c=list(a.union(b))
d=list(a.intersection(b))
c.sort()
d.sort()
for x in c:
    print(x,end=' ')
print()
for x in d:
    print(x,end=' ')

