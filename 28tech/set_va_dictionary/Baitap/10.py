n=int(input())
a=list(map(int,input().split()))
s=set({})
b=[0]*n
for i in range(n-1,-1,-1):
    x=a[i]
    s.add(x)
    b[i]=len(s)
for i in range(int(input())):
    q=int(input())
    print(b[q])
