# list cac so nguyen
a= [1,2,3,4]
print(a)
# list cac string
b=["28 tech", "Quang Anh","con cho"]
print(b)
#list linh tinh
c=[1,2,3,5.6,"ha ha"]
print(c)
#list constructor
s="28tech"
d=list(s)
print(d)
e=list(range(20))
print(e)
#thao tac
print(len(a))
print(b[1],c[-2])
for i in c:
    print(i,end=" ")
print()
for i in range(len(a)-1,-1,-1):
    print(i,end=" ")
print(a)
a[2]="28 tech"
print(a)
#them 1 phan tu vao cuoi list
a.append(10)
print(a)
#them vao vi tri bat ki
#chen 100 vao vi tri 2
a.insert(2,100)
#chen 200 vao vi tri n-2
a.insert(-2,200)
print(a)
#xoa  phan tu cuoi khoi list
a.pop()
print(a)
#xoa phan tu chi dinh
a.pop(1)
print(a)
#xoa gia tri dau tien
a.remove(200)
print(a)
#sao chep list
a2=a*2
print(a2)
so=[0]*10
print(so)
#kiem tra mot gia tri co trong list khong: O(n)
if 5 in a:
    print("YEs")
else: print("NO")    
#lien ket hai list lai voi nhau
so1=[1,2,3,4]
so2=[5,6,7,8]
so1+=so2
print(so1)
so1.extend(so2)
print(so1)
#phuong thuc
#ham copy:
a=[1,2,3]
b=a.copy()
print(b)
#ham count(): tra ve so lan xuat hien cua 1 phan tu
print(a.count(1))
#ham index(): tra ve chi so dau tien cua phan tu:
print(a.index(2))
#ham revrese
a.reverse()
print(a)
#ham sort(): O(NlogN)
a.sort()
print(a)
#ham built-in
print(max(a),min(a),sum(a),all(a),any(a))
print(sorted(a))   #Tra ve mot ham sap xep nma a vẫn giữ nguyên

