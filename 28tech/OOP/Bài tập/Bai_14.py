from functools import cmp_to_key
def cmp(a,b):
    dob_a=a.get_dob()
    dob_b=b.get_dob()
    if dob_a!=dob_b:
        da=dob_a.split('/')
        db=dob_b.split('/')
        if da[2]<db[2]: return -1
        elif da[2]>db[2]: return 1
        
        if da[1]<db[1]: return -1
        elif da[1]>db[1]:return 1
        
        if da[0]<db[0]: return -1
        elif da[0]>db[0]: return 1
    else:
        ma_a=a.get_ma()
        ma_b=b.get_ma()
        if ma_a<ma_b: return -1
        else: return 1
class NhanVien:
    def __init__(self,ma,ten,gt,dob,diachi,mathue,hopdong):
        self.ma = ma
        self.ten = ten
        self.gt = gt
        self.dob=dob
        self.diachi=diachi
        self.mathue = mathue
        self.hopdong = hopdong
        self.ma = format(ma,'05d')
        
        if self.dob[2]!='/':self.dob="0"+self.dob
        if self.dob[5]!= '/': self.dob = self.dob[:3]+"0"+self.dob[3:]
        if self.hopdong[2]!='/':self.hopdong="0"+self.hopdong
        if self.hopdong[5]!= '/': self.hopdong = self.hopdong[:3]+"0"+self.hopdong[3:]
    def __str__(self):
        return f'{self.ma} {self.ten} {self.gt} {self.dob} {self.diachi} {self.mathue} {self.hopdong} '
    def get_dob(self):
            return self.dob
    def get_ma(self):
        return self.ma
n=int(input())
a=[]
for i in range(n):
    m=NhanVien(i+1,input(),input(),input(),input(),input(),input())
    a.append(m)
a.sort(key=cmp_to_key(cmp))
for x in a:
    print(x)
    