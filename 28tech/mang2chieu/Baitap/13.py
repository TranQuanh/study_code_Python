m,n,p=map(int,input().split())
a=[]
b=[]
for i in range(m):
    c=list(map(int,input().split()))
    a.append(c)
for i in range(n):
    c=list(map(int,input().split()))
    b.append(c)
c=[[0 for i in range(p)] for i in range(m)]
for i in range(m):
    for j in range(p):
        for k in range(n):
            c[i][j]+=a[i][k]*b[k][j]
for i in range(m):
    for j in range(p):
        print(c[i][j],end=' ')
    print()