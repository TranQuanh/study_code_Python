from math import comb
from collections import Counter
s=input()
a=dict(Counter(s))
dem=len(s)
for x,y in a.items():
    dem+=comb(y,2)
print(dem)