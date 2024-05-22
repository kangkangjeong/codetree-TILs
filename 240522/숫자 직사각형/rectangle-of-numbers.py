n,m=map(int,input().split())
arr2D=[
    [0 for _ in range(m)]
    for _ in range(n)
]

num=1
for i in range(n):
    for j in range(m):
        arr2D[i][j]=num
        num+=1
for row in arr2D:
    for col in row:
        print(col,end=' ')
    print()