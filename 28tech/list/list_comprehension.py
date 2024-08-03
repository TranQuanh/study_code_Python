from math import *
def sum_digit(n):
    res=0
    while n:
        res+=n%10
        n//=10
    return res;    
def nt(n):
    for i in range(2,isqrt(n)+1):
        if(n%i==0) :return False
    return True    
a=[1,2,3,4,5,6,7]
b= [x+3 for x in a]
print(b)
c=[x**3 for x in range(5)]
print(c)
a=[101,2423,352,653]
b=[sum_digit(x) for x in a]
print(b)
#if
a=[1,2,3,-4,5,-6]
b=[x for x in a if x>0]
print(b)
a=[2,3,4,5,6,7]
c=[x for x in a if nt(x)]
print(c)
