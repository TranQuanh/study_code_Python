n=int(input())
a=list(map(int,input().split()))
max1,max2=-10**18,-10**18
for x in a:
    if max1>x:
        x=max1
        max2=max1
    elif max2>x:
        max2=x
print(max1,max2)