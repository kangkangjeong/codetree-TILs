def print_square(n):
    current_number = 1  # 시작 숫자

    for i in range(n):  # N개의 행을 반복
        row = []  # 각 행을 저장할 리스트
        for j in range(n):  # N개의 열을 반복
            row.append(current_number)  # 현재 숫자를 행에 추가
            current_number += 1  # 다음 숫자로 증가
            if current_number > 9:  # 9를 넘어가면 1로 초기화
                current_number = 1
        print(' '.join(map(str, row)))  # 행을 공백으로 구분하여 출력

# 입력 받기
N = int(input())
print_square(N)