def sum_digit(n):
    tong=0
    while n:
        tong+=n%10
        n//=10
    return tong    
    
a=["28tech","python","java","c++"]
a.sort()
print(a)
a=[3,2,1,5,4]
a.sort(reverse=True)
print(a)
a=[-2,-3,-1,3,5,1]
a.sort(key=abs)
print(a)
#stable
a=[333,123,423,414,53,63,10,100,11,2]
a.sort(key=sum_digit)
print(a)
#lambda
a=[-2,-3,-2,1,5]
a.sort(key=lambda x:(abs(x),x))
print(a)
a=[[1,2],[3,2],[4,1],[5,6]]
a.sort(key=lambda x: (x[0],x[1]))
print(a)
a=[[1,2],[3,2],[4,1],[5,6]]
a.sort(key=lambda x: (x[0],-x[1]))
print(a)
a.sort(key=abs)