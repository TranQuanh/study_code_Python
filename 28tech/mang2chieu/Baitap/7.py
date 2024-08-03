a=[]
n=int(input())
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
x,y=map(int,input().split())
x-=1
y-=1
a[x],a[y]=a[y],a[x]
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()