n=int(input())
a=list(map(int,input().split()))
cnt=[0]*(10**6+1)
for x in a:
    cnt[x]  =1
dem=0
for i in range(0,10**6+1):
    dem+=cnt[i]
    