F=[0]*(10**6+1)
m=10**9+7
def init():
    F[0]=0
    F[1]=0
    F[2]=1
    for i in range(3,10**6+1):
        F[i]=F[i-1]+F[i-2]+F[i-3]
        F[i]%=m
init()
for i in range(int(input())):
    n=int(input())
    print(F[n])