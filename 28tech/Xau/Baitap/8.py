from collections import Counter
s=input()
s=s.lower()
a=dict(Counter(s))
print("YES" if len(a)==26 else"NO")