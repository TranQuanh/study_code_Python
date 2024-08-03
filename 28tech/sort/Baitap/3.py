def tong(n):
    tong=0
    while n:
        tong+=n%10
        n//=10
    return tong
n=int(input())
a=list(map(int,input().split()))

a.sort(key=lambda x:[tong(x),x])
print(a)