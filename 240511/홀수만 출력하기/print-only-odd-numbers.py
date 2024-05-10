# 입력 받기
N = int(input())  # 정수 N 입력 받음

# N번 반복하여 입력 받은 정수 중 홀수이면서 3의 배수인 수 출력
for _ in range(N):
    num = int(input())
    if num % 2 == 1 and num % 3 == 0:  # 홀수이면서 3의 배수인지 확인
        print(num)