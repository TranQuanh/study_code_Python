class SV:
    def __init__(self,ma,ten,lop,db,diem):
        ma=str(ma)
        while len(ma)<3:
            ma="0"+ma
        ma="SV"+ma
        if db[2] !='/': db="0"+db
        if db[5]!='/':db=db[:3]+'0'+db[3:]
        self.ma=ma
        self.ten=ten
        self.lop=lop
        self.db=db
        self.diem=diem
    def __str__(self):
        return f'{self.ma} {self.ten} {self.lop} {self.db} {self.diem:.2f}'
    
n=int(input())
a=[]
for i in range(n):
   m=SV(i+1,input(),input(),input(),float(input()))
   a.append(m)
for x in a:
    print(x)         