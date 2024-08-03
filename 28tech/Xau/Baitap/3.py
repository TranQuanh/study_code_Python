from collections import Counter
s=input()
a=dict(Counter(s))
for x,y in sorted(a.items()):
    print(x,y)
print()
for x,y in a.items():
    print(x,y)
