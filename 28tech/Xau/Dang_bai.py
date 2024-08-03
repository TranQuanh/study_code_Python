from collections import Counter
# Dạng 1: tuần suất
# Cach 1 đánh dấu
s='28 tech python 28 tech aaaaba'
# ascii:0->256
cnt=[0]*256
for x in s:
    cnt[ord(x)]+=1
for i in range(256):
    if cnt[i]!=0:
        print(chr(i),cnt[i])
for x in s:
    if cnt[ord(x)]!=0:
        print(x,cnt[ord(x)])
        cnt[ord(x)]=0
# Cach 2: dictionary
d=dict({})
for x in s:
    if x in d:
        d[x]+=1
    else: d[x]=1
for x,y in d.items():
    print(x,y)  
for x,y in sorted(d.items()):
    print(x,y)
# cach 3: counter
d=dict(Counter(s))
print(d)