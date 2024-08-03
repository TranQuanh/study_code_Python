n=int(input())
a=list(map(int,input().split()))
sochan,sole,tongchan,tongle=0,0,0,0
for x in a:
    if x%2==0:
        sochan+=1
        tongchan+=x
    else:
        sole+=1
        tongle+=x
print(sochan,sole,tongchan,tongle,sep="\n")
