from functools import cmp_to_key
# -1 1 0
# a đứng trước, b đứng sau sau khi sắp xếp
# Nếu a và  b đã đúng thứ tự mà bạn muốn thì trả về -1, ngược lại trả về 1
def cmp(a,b):
    if a<b: return -1
    elif a>b: return 1
    else :return 0
def cmp2(a,b):
    return a-b
# sắp xếp theo tổng
def tong(n):
    sum=0
    while n:
        sum+=n%10
        n//=10
    return sum
def cmp3(a,b):
    tong1,tong2=tong(a),tong(b)
    if(tong1!=tong2):
        return tong1-tong2  
    else:
        return a-b   
a =[10,2,3,1,1,4,5,6,3,8]
a.sort(key=cmp_to_key(cmp))
print(a)
a=[3000,12,21]
a.sort(key=cmp_to_key(cmp3))
print(a)