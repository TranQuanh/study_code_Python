from collections import Counter
s=input()
s=s.split()
a=dict(Counter(s))
for x,y in sorted(a.items()):
    print(x,end=' ')
print()
for x,y in a.items():
    print(x,end=' ')
