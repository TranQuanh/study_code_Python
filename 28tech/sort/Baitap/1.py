n=int(input())
a=list(map(int,input().split()))
a.sort()
dem=1
for i in range(1,n-1):
    if a[i]!=a[i+1]:dem+=1
print(dem)