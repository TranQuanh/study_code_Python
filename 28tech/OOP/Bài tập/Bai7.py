class NhanVien:
    def __init__(self,ma,ten,luong,ngay,chuc):
        self.ma=ma
        self.ten=ten
        self.luong=luong
        self.ngay=ngay
        self.chuc=chuc
    def __str__(self):
        luongthang = self.luong*self.ngay
        ngay=self.ngay
        thuong=0
        if ngay>=25: thuong = 25/100
        elif ngay>=22: thuong =10/100
        tongthuong=luongthang*thuong
        tong=luongthang+tongthuong
        chuc=self.chuc
        if chuc=="GD": phu=250000
        elif chuc=="PGD":phu=200000
        elif chuc=="TP":phu=180000
        elif chuc=="NV":phu=150000
        tong+=phu
        
        return f'{self.ma} {self.ten} {luongthang} {tongthuong} {phu} {tong}'
a=NhanVien("NV01",input(),int(input()),int(input()),input())
print(a)