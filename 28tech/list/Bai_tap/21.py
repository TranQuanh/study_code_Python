n=int(input())
a=list(map(int,input().split()))
cnt=[0]*1001
for x in a:
    cnt[x]+=1
cnt2=cnt.copy()
for x in a:
    if cnt[x]!=0:
        print(x,cnt[x])
        cnt[x]=0
l=min(a)
r=max(a)
for i in range(min(a),max(a)+1):
    if cnt2[i]:
        print(i,cnt2[i])
max_fre,max_val=0,0
for x in range(l,r+1):
    if cnt2[x]>=max_fre:
        max_fre=cnt2[i]
        max_val=i
min_fre,min_val=10**9,0
for x in range(l,r+1):
    if cnt2[x]<min_fre:
        min_fre=cnt2[x]
        min_val=x
    
