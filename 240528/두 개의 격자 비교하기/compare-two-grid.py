n, m = map(int, input().split())
arr2d_1 = [
    list(map(int, input().split()))
    for _ in range(n)  # n으로 변경
]
arr2d_2 = [
    list(map(int, input().split()))
    for _ in range(n)  # n으로 변경
]
arr2d_new = [
    [1 for _ in range(m)]  # 초기값을 0으로 설정
    for _ in range(n)
]

for index1 in range(n):
    for index2 in range(m):
        if arr2d_1[index1][index2] == arr2d_2[index1][index2]:
            arr2d_new[index1][index2] = 0

for row in arr2d_new:
    print(*row)