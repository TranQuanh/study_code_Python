n=int(input())
a=list(map(int,input().split()))
b=set({})
for x in a:
    if x not in b:
        print(x,end=' ')
        b.add(x)

        