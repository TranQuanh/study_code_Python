n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
dem=1
gioihan=10**9
for i in range(1,n):
    if gioihan<=0: break
    gioihan=min(gioihan-1,a[i])
    dem+=1
print(dem)
    