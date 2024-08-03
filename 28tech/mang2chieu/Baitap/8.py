a=[]
n=int(input())
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
x,y=map(int,input().split())
x-=1
y-=1
for i in range(n):
    a[i][x],a[i][y]=a[i][y],a[i][x]
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
