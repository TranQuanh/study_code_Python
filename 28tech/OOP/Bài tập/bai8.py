class ThiSinh:
    def __init__(self,ma,ten,toan,li,hoa):
        self.ma=ma
        self.ten=ten
        self.toan=toan
        self.li=li
        self.hoa=hoa
    def infor(self):
        tong=self.toan+self.li+self.hoa
        uutien=self.ma[:-1]
        diemcong=0
        if uutien =="KV1": diemcong=0.5
        elif uutien=="KV2":diemcong=1.0
        elif uutien=="KV3":diemcong=1.5
        tong+=diemcong
        so=self.ma[-2]
        res=""
        if tong>=24:res="TRUNG TUYEN"
        else: res="TRUOT"
        print(self.ma +" "+self.ten+" "+ so ,end=" ")
        if tong==int(tong):print(int(tong),end=" ")
        else:print("%.1f"%tong,end=" ")
        print(res)
    
a=ThiSinh(input(),input(),float(input()),float(input()),float(input()))
a.infor()