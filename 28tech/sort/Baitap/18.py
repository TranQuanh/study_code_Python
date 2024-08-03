n,s=map(int,input().split())
a=[]
for i in n:
    b=list(map(int,input().split()))
    a.append(b)
dem=0
a.sort(key=lambda x:x[0])
for x,y in a:
    if s>x:
        s+=y
    else:
        print("NO")
        exit()
    print("YES")
