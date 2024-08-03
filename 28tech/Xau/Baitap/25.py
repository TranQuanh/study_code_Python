m,s=map(int,input().split())
if m*9<s or (s==0 and m>1):
    print("NOT FOUND")
else:
    lon=[0]*m
    be=[0]*m
    t=s
    t-=1
    for i in range(m):
        if s>9:
            lon[i]=9
            s-=9
        else:
            lon[i]=s
            s=0
    for i in range(m-1,0,-1):
        if t>9:
            be[i]=9
            t-=9
        else:
            be[i]=t
            t=0
    be[0]=1
    be[0]+=t
    for x in lon:
        print(x,end='')
    print()
    for x in be:
        print(x,end='')