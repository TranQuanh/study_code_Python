F=[0]*(10**6+1)
m=10**9+7
def init():
    F[0]=1
    F[1]=1
    for i in range (2,10**6+1):
        F[i]=F[i-1]*i
        F[i]%=m
init()
for i in range(int(input())):
    n=int(input())
    print(F[n])