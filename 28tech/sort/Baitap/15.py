n=int(input())
a=list(map(int,input().split()))
cnt=[0]*(10**6+1)
for x in a:
    cnt[x]+=1
minn=min(a)
maxn=max(a)
ans=0
for i in range(minn,maxn+1):
    if cnt[i]==0:
        ans+=1
print(ans)