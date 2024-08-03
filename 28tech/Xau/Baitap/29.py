s=input()
t=""
for x in s:
    if x.isalpha():
        t+=" "
    else:
        t+=x
t=list(map(int,t.split()))
print(sum(t))