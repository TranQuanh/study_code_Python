from math import gcd
class PhanSo:
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
    def DonGian(self):
        chung=gcd(self.tu,self.mau)
        self.tu=self.tu//chung
        self.mau=self.mau//chung
    def __str__(self):
        return f'{self.tu}/{self.mau}'
tu,mau=map(int,input().split())
p1=PhanSo(tu,mau)
p1.DonGian()
print(p1)