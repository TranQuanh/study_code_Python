a=[[1,2,3],[4,5,6],[7,8,9]]
n,m=map(int,input().split())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)

a=[[0 for i in range(m)] for i in range(n)]
print(a)
a=[[1,2,3],[4,5,6]]
b=[j for i in a for j in i]
print(b)

a=[[1,2,3],[3,4,5],[5,6,7]]
a_t=[[row[i] for row in a]for i in len(a[0])]
a=[[1,2,3],
   [3,4,5],
   [4,5,6]]
path=[[-1,-1],[-1,0],[-1,1],
      [0,-1],[0,1],
      [1,-1],[1,0],[1,1]]
i,j=1,1
for x in path:
    i1,j1=i+x[0],j+x[1]
    print(a[i1][j1],end=' ')
a=[[1,2,3],[3,4,5],[5,6,7]]
a_t=[[row[i] for row in a] for i in len(a[0])]
