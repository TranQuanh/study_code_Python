a=[]
n=int(input())
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
b=[[0 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        b[j][i]=a[i][j]
for i in range(n):
    b[i].sort()
for i in range(n):
    for j in range(n):
        print(b[j][i],end=' ')
    print()