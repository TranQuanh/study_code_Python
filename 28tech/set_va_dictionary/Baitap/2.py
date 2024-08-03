n=int(input())
a=list(map(int,input().split()))
b={x:1 for x in a}
for i in range(int(input())):
    so=int(input())
    if so in b:
        print("YES")
    else: print("NO")
    
# lưu ý tìm kiếm trong set với dict chỉ mất O(1) 