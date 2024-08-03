n=int(input())
a=list(map(int,input().split()))
k=int(input())
dem=0
for i in range(0,n):
    for j in range(i,n):
        if a[i]+a[j]==k:
            dem+=1
print(dem)