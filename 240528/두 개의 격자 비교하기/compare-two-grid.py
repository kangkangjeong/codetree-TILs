n,m=map(int,input().split())
arr2d_1=[
    list(map(int,input().split()))
    for _ in range(m)
]
arr2d_2=[
    list(map(int,input().split()))
    for _ in range(m)
]
arr2d_new=[
    [1 for _ in range(m)]
    for _ in range(n)
]
for index1,i in enumerate(arr2d_1):
    for index2,j in enumerate(arr2d_2):
        if arr2d_1[index1][index2]==arr2d_2[index1][index2] :
            arr2d_new[index1][index2]=0
for k in (arr2d_new):
    print(*k)