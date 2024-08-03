n=int(input())
a=list(map(int,input().split()))
d=dict({})
for x in a:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
for i in range(int(input())):
    tt,x=map(int,input().split())
    if tt==1:
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    elif tt==2:
        if x in d:
            d[x]-=1
            if d[x]==0:
               d.pop(x)
    elif tt==3:
        if x in d: print("YES")
        else:print("NO")
        