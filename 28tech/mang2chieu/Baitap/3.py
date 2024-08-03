a=[]
n,m=map(int,input().split())
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
minn,maxn=10**10,-10**10
for i in range(n):
    minn=min(minn,min(a[i]))
    maxn=max(maxn,max(a[i]))
print(minn)
for i in range(n):
    for j in range(m):
        if a[i][j]==minn: print(i+1,j+1)
print(maxn)
for i in range(n):
    for j in range(m):
        if a[i][j]==maxn: print(i+1,j+1)