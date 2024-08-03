n=int(input())
a=list(map(int,input().split()))
F=[0]*(n)
for i in range(n):
    if i==0: F[0]=a[0]
    else:
        F[i]=F[i-1]+a[i]
print(F)
