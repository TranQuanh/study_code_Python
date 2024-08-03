from functools import cmp_to_key
def cmp(a,b):
    if a.get_gpa() !=b.get_gpa():
        return b.get_gpa()-a.get_gpa()
    else:
        ma_a=a.get_ma()
        ma_b=b.get_ma()
        if ma_a <ma_b: return -1
        else: return 1
class SinhVien:
    def __init__(self,ma,ten,nganh,dob,diem):
        self.ma= ma
        self.ten = ten
        self.nganh = nganh
        self.dob= dob
        self.diem = diem
        self.ma = format(ma,'03d')
        self.ma = "SV"+self.ma
        if self.dob[2] != '/':self.dob="0"+self.dob
        if self.dob[5] !='/':self.dob=self.dob[:3]+"0"+self.dob[3:]
        
        tmp = self.ten.split()
        self.ten = ' '.join(tmp).title()
    def __str__(self):
        return f'{self.ma} {self.ten} {self.nganh} {self.dob} {self.diem}'
    def get_ma(self):
        return self.ma
    def get_gpa(self):
        return self.diem
n=int(input())
a=[]
for i in range(n):
    m=SinhVien(i+1,input(),input(),input(),float(input()))
    a.append(m)
a.sort(key=cmp_to_key(cmp))
# a.sort(key=lambda x:[-(x.get_gpa()),x.get_ma()])
for x in a:
    print(x)