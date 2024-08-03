m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
dem=0
i,j=0,0
while i<m and j<m:
    if a[i]>b[j]:
        dem+=1
        i+=1
        j+=1
    else:
        i+=1
print(dem)