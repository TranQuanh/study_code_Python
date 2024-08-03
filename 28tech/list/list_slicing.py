#a[start,stop,step]
a=[1,2,3,4,5]
b=a[2:5:1]
c=a[:5]
print(b)
print(c)
#reverse list
print(a[::-1])
#thay doi list
a[2:4]=[4,5]
print(a)
a[2:4]=[]
print(a)
#chen 
a[:0]=[1,2,3]
a[len(a):]=[1,2,3]
print(a)
#them vao giua list
a[2:2]=['X','Y','Z']
print(a)