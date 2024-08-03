func= lambda x: x**2
print(func(10))
res=(lambda x:x**2)(10)
print(res)
b= lambda x,y,z:x+y+z
print(b(100,200,300))
c=lambda x=200,y=100,z=300:x+y+z
a=[1,2,3,4]
#map
d=list(map(lambda x:x**2,a))
print(d)
#filter
e=list(filter(lambda x:x%2==0,a))
print(e)
# if else
findMax = lambda x,y: x if x>y else y
print(findMax(100,200))
