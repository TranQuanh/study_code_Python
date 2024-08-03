s=input()
diem=1
so=s[0]
diemmax=0
res=s[0]
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        if diemmax<diem:
            diemmax=diem
            res=so
        elif diemmax==diem:
            if res<so:
                res=so
        diem=1
        so=s[i]
    else:
        diem +=1
        so+=s[i]
if diemmax<diem:
    diemmax=diem
    res=so
elif diemmax==diem:
    if res<so:
        res=so
print(res)  