b,c=map(int,input().split())
B=list(map(int,input().split()))
C=list(map(int,input().split()))
x,y=0,0
while x<b and y<c:
    if B[x]<=C[y]:
        print("b",x+1,sep="",end=" ")
        x+=1
    else:
        print("c",y+1,sep="",end=" ")
        y+=1
while x<b:
    print("b",x+1,sep="",end=" ")
    x+=1
while y<c:
    print("c",y+1,sep="",end=" ")
    y+=1
