class SinhVien:
    def __init__(self,ten,dob,diem1,diem2,diem3):
        self.ten=ten
        self.dob=dob
        self.diem1=diem1
        self.diem2=diem2
        self.diem3=diem3
        if (self.dob[2]!='/'): self.dob='0'+self.dob
        if self.dob[6]!='/': self.dob=self.dob[:3]+'0'+dob[3:]
    def __str__(self):
        tongdiem=diem1+diem2+diem3
        return f'{self.ten} {self.dob} {tongdiem:.1f}'
    
ten=input()
dob=input()
diem1=float(input())
diem2=float(input())
diem3=float(input())
p1=SinhVien(ten,dob,diem1,diem2,diem3)
print(p1)
        