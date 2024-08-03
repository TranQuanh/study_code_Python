from collections import Counter
s=input()
s=s.split()
a=dict(Counter(s))
minn,maxn=10**9,-10**9
mina,maxa='a','a'
for x,y in sorted(a.items()):
    if minn >=y:
        minn=y
        mina=x
    if maxn <=y:
        maxn=y
        maxa=x
print(mina,maxa)