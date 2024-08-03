s="python"
len=0
t=input()
for x in t:
    if x==s[len]:
        len+=1
    if len==6:
        print("YES")
        exit()
print("NO")