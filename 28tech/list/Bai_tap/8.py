n=int(input())
a=list(map(int,input().split()))
cnt=[0]*(10^3+1)
for x in a:
    if cnt[x]==0:
        print(x,end=" ")
        cnt[x]=1

        