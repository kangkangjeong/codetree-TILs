# 5x5 크기의 배열을 초기화
size = 5
matrix = [[0] * size for _ in range(size)]

# 첫 번째 행과 첫 번째 열을 1로 초기화
for i in range(size):
    matrix[0][i] = 1
    matrix[i][0] = 1

# 나머지 칸들을 바로 위의 값과 바로 왼쪽의 값을 더해서 채움
for i in range(1, size):
    for j in range(1, size):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

# 출력
for row in matrix:
    print(' '.join(map(str, row)))