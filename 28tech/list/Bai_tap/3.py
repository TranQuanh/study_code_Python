n=int(input())
a=list(map(int,input().split()))
benhat=min(a)
tong=0
for x in a:
    if x==benhat: tong+=1
print(tong)
    