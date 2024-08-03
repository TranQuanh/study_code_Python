n=int(input())
a=list(map(int,input().split()))
x=int(input())
lon=0
nho=0
for y in a:
    if y<x: nho+=1
    elif y>x: lon+=1
print(nho,lon,sep=" ")