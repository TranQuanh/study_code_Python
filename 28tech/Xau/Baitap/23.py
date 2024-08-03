from functools import cmp_to_key
def cmp(a,b):
    tonga=a+b
    tongb=b+a
    if tonga>tongb: return -1
    else: return 1
n=int(input())
a=input().split()
a.sort(key=cmp_to_key(cmp))
print(' '.join(a))

