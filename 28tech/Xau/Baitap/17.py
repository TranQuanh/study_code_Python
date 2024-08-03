s=input()
s=s.title().split()
s[-1]=s[-1].upper()
for i in range(len(s)-1):
    print(s[i],end='')
    if i==len(s)-2:print(", ",end='')
    else:print(" ",end='')
    
print(s[-1])
print(s[-1],", ",end='',sep='')
for i in range(0,len(s)-1):
    print(s[i],end=' ')
