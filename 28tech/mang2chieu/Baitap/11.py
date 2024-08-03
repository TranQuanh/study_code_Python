a=[]
n=int(input())
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
for i in range(n):
    a[i].sort()
    for j in range(n):
        print(a[i][j],end=' ')
    print()
