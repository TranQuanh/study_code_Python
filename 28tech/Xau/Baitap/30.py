from functools import cmp_to_key
def cmp(a,b):
    ab=a+b
    ba=b+a
    if ab>ba: return -1
    else: return 1
s=input()
t=""
for x in s:
    if x.isalpha():
        t+=" "
    else:
        t+=x
t=list(map(int,t.split()))
t=list(map(str,t))
print(t)
t.sort(key=cmp_to_key(cmp))
print(''.join(t))