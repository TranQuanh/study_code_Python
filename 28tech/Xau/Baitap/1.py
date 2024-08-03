s=input()
chucai,chuso,dacbiet=0,0,0
for x in s:
    if x.isdigit(): chuso+=1
    elif x.isalpha(): chucai+=1
    else:dacbiet+=1
print(chucai,chuso,dacbiet,sep='\n')
