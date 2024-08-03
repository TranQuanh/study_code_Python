n=int(input())
a=list(map(int,input().split()))
dau=0
for i in range(0,len(a),2):
    if a[i]%2==0:
        print(a[i],end=" ")
        dau=1
if dau==0: print("NONE")