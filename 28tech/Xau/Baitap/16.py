ten=input()
db=input()
ten=ten.split()
ten=' '.join(ten)
print(ten.title())
if(db[2]!='/'):db="0"+db
if(db[5]!='/'):db=db[:3]+'0'+db[3:]
print(db)