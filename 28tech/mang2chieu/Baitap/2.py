a=[]
n,m=map(int,input().split())
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
for i in range(n):
    so=sum(a[i])
    print(so,end=' ')
print()
for j in range(m):
    so=0
    for i in range(n):
        so+=a[i][j]
    print(so,end=' ')
    