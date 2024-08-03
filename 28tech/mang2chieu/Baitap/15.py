fibo=[0]*101
def init():
    fibo[0]=0
    fibo[1]=1
    for i in range(2,101):
        fibo[i]=fibo[i-1]+fibo[i-2]
init()
n=int(input())
a=[[0 for i in range(n)] for i in range(n)]
h1,h2,c1,c2=0,n-1,0,n-1
dem=0
while h1<=h2 and c1<=c2:
    for i in range(c1,c2+1):
        a[h1][i]=fibo[dem]
        dem+=1
    h1+=1
    for i in range(h1,h2+1):
        a[i][c2]=fibo[dem]
        dem+=1
    c2-=1
    for i in range(c2,c1-1,-1):
        a[h2][i]=fibo[dem]
        dem+=1
    h2-=1
    for i in range(h2,h1-1,-1):
        a[i][c1]=fibo[dem]
        dem+=1
    c1+=1
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()