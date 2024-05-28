def fill_zigzag(n, m):
    matrix = [[0] * m for _ in range(n)]
    num = 0
    
    for col in range(m):
        if col % 2 == 0:
            for row in range(n):
                matrix[row][col] = num
                num += 1
        else:
            for row in range(n-1, -1, -1):
                matrix[row][col] = num
                num += 1
    
    for row in matrix:
        print(' '.join(map(str, row)))

# 입력 받기
n, m = map(int, input().split())
fill_zigzag(n, m)