a=[]
n=int(input())
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
for i in range(n):
    a[i][i],a[i][n-i-1]=a[i][n-i-1],a[i][i]
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()