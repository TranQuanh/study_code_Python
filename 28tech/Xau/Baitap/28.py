s=input()
maxn=-10**9
diem="0"
s=s+"o"
for x in s:
    if x.isdigit():
        diem+=x
    else:
        res=int(diem)
        maxn=max(maxn,res)
        diem="0"
print(maxn)