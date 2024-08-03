n=int(input())
a=list(map(int,input().split()))
ma,mi=max(a),min(a)
for i in range(n):
    if a[i] ==mi:
        miin=i
for i in range(n):
    if a[i]==ma:
        main=i
        break
print(main,miin)