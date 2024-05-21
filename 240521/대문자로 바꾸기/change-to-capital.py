# 입력 받기
input_matrix = []
for _ in range(5):
    row = input().split()
    input_matrix.append(row)

# 대문자로 변환
output_matrix = []
for row in input_matrix:
    output_row = [char.upper() for char in row]
    output_matrix.append(output_row)

# 출력
for row in output_matrix:
    print(' '.join(row))