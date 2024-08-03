class SoPhuc:
    def __init__(self,thuc,ao):
        self.thuc = thuc
        self.ao = ao
    def __add__(self,other):
        thuc =self.thuc+other.thuc
        ao = self.ao+other.ao
        return SoPhuc(thuc,ao)
    def __str__(self):
        return f'{self.thuc} + {self.ao}j'
    def __sub__(self,other):
        pass
    def __mul__(self,other):
        pass
    def __truediv__(self,other):
        # nap chong toan tu chia: chia nguyen
        pass
    
    # toan tu so sanh 
    def __lt__(self,other):
        # dau <
        if self.phuc < other.phuc:
            return 1
        else : return 0
    def __le__(self,other):
        # dau <=
        pass
    def __gt__(self,other):
        # dau >
        pass
    def __ge__(self,other):
        # dau >= 
        pass
    def __eq__(self,other):
        # dau ==
        pass
    def __ne__(self,other):
        # dau != 
        pass
p1=SoPhuc(1,2)
p2= SoPhuc(2,3)
p3=p1+p2
print(p3)