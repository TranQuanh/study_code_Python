def even(n):
    return n%2==0
#map
a=[-100,200,300,-400]
a=list(map(lambda x:x**2,a))
print(a)
a=['A','B','C']
a=list(map(ord,a))
print(a)
a=[1,2,3,4]
b=[5,6,7,8]
c=list(map(lambda x,y:x+y,a,b))
print(c)
#filter
a=[1,2,3,4,5,6,7,8]
b=list(filter(even,a))
c=list(filter(lambda x:x%2==1,a))
print(b)
print(c)