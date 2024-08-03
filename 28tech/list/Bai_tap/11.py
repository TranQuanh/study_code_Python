Fibo=[0]*100
def sieve():
    Fibo[0]=0
    Fibo[1]=1
    for i in range(2,100+1):
        Fibo[i]=Fibo[i-1]+Fibo[i-2]
sieve
n=int(input())
a=list(map(int,input().split()))
check=True
for x in a:
    if x in Fibo:
        print(x,end=" ")
        check= False
if check: print("None")
