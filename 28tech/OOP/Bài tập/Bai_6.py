class GiaoVien:
    def __init__(self,ma,ten,luong):
        self.ma=ma
        self.ten=ten
        self.luong=luong
    def __str__(self):
        heso={'HT':2000000,
              'HP':900000,
              'GV':500000}
        thuong=heso[self.ma[:2]]
        nhan=int(self.ma[-1])
        tong=self.luong*nhan+thuong
        return f'{self.ma} {self.ten} {nhan} {tong}'
a=GiaoVien(input(),input(),int(input()))
print(a)
        