def tn(s):
    rev=s[::-1]
    return s==rev
s=input()
se=set({})
t=[]
s=s.split()
for x in s:
    if tn(x):
        if x not in se:
            t.append(x)
            se.add(x)
t.sort(key=lambda x:[len(x)])
print(' '.join(t))