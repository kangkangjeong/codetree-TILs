n=int(input())
arr_2d=[
    [0 for _ in range(n)]
    for _ in range(n)
]

num=1
for i in range(1,n+1):
    for j in range(1,n+1):
        arr_2d[i-1][j-1]=num
        num+=n
    num=i+1
for k in arr_2d:
    print(*k)