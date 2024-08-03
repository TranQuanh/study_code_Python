n,x=map(int,input().split())
a=map(int,input().split())
if x in a:
    a.pop(a.index(x))
    for b in a:
        print(b,end=' ')
else:
    print("NOT FOUND")