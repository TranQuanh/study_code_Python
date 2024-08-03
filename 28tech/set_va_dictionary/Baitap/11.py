from collections import Counter
n=int(input())
a=list(map(int,input().split()))
b=list(dict(Counter(a)).items())
c=b
c.sort(key=lambda x:x[0])
for x,y in c:
    print(x,y)
print()
for x,y in b:
    print(x,y)
    

