a, b = map(int, input().split())

# 모든 결과를 바로 세로로 출력하기 위해 가장 바깥쪽 반복문을 짝수 배수에 대해 설정
for j in range(2, 9, 2):  
    # 다음으로 내부에서 a부터 b까지 반복하면서 각 곱셈 결과를 출력
    for i in range(b, a - 1, -1):  
        if i > a:  # 첫 번째 수가 아니라면, 줄 바꿈 없이 ' / '와 함께 출력
            print(f'{i} * {j} = {i*j}', end=' / ')
        else:  # 첫 번째 수일 경우 줄 바꿈과 함께 출력
            print(f'{i} * {j} = {i*j}')