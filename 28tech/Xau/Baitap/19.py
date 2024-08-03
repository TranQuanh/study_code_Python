d=dict({})
for i in range(int(input())):
    line=list(input().split())
    ten=line[:-1]
    db=line[-1]
    email=ten[-1].lower()
    for i in range(0,len(ten)-1):
        email+=ten[i][0].lower()
    if email not in d:
        d[email]=1
        email+="@xyz.edu.vn"
    elif email in d:
        d[email]+=1
        email+=str(d[email])+"@xyz.edu.vn"
    print(email)
    db=map(int,db.split('/'))
    for i in db:
        print(i,end='')
    print()

