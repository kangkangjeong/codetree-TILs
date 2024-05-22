# 입력을 받습니다.
arr1 = []
arr2 = []

for _ in range(3):
    arr1.append(list(map(int, input().split())))
n= input()
for _ in range(3):
    arr2.append(list(map(int, input().split())))

# 두 배열의 곱을 저장할 결과 배열을 생성합니다.
result = [[0 for _ in range(3)] for _ in range(3)]

# 두 배열의 같은 위치에 있는 요소들의 곱을 계산합니다.
for i in range(3):
    for j in range(3):
        result[i][j] = arr1[i][j] * arr2[i][j]

# 결과 배열을 출력합니다.
for row in result:
    print(" ".join(map(str, row)))