infor={
    'name':'28tech',
    'job':'it',    
}
print(infor)
a=[['con cho','Quang'],['con lon','Dung']]
b=dict(a)
print(b)

a=['con cho','con lon']
b=['Quang','Dung']
c=dict(zip(a,b))
print(c)

a=['a','b','c']
defaultvalue=0
b=dict.fromkeys(a,defaultvalue)
print(b)
# key trong dictionary là duy nhất
# key không thẻ thay đổi
a={1:'ha ha',2:'con cho',3:'con lonw'}
print(a[1])
print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))
# check key chỉ mất 0(1)
for i in a.keys():
    print(i,a[i])
for key,value in a.items():
    print(key,value)
a[4]='con ngua'
print(a)
a.pop(4)
print(a)
a={}
a[-1]=1
print(a)
a=[1,2,3,4,5]
b=[[x,x**2] for x in a]
print(b)
c=list(map(lambda x:[x,x**2],a))
print(c)
a={x:x**2 for x in range(0,5)}
print(a)