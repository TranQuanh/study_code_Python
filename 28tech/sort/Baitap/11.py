n=int(input())
a=list(map(int,input().split()))
dem=0
for i in range(0,n):
    if a[i]-i<=0: break
    dem+=a[i]-i
print(dem)