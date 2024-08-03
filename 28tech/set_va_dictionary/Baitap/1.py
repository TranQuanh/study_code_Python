n=int(input())
a=list(map(int,input().split()))
# a=set(a)
# print(len(a))
b=dict({})
for x in a:
        b[x]=1
print(len(b))