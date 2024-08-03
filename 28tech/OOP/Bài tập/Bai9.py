class Hang:
    def __init__(self,ma,ten,donvi,mua,ban):
        ma=str(ma)
        while len(ma)<4:
            ma="0"+ma
        ma="M"+ma
        self.ma=ma
        self.ten=ten
        self.donvi=donvi
        self.mua=mua
        self.ban=ban
        
    def get_loi_nhuan(self):
        return self.ban-self.mua
    def get_ma(self):
        return self.ma
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.donvi} {self.mua} {self.ban} {self.ban-self.mua}'
    
n=int(input())
a=[]
for i in range(n):
   m=Hang(i+1,input(),input(),int(input()),int(input()))
   a.append(m)
a.sort(key=lambda x:[-x.get_loi_nhuan(),x.get_ma()])
for i in range(n):
    print(a[i])
  