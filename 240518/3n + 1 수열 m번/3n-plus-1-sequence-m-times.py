# m 입력 받기
m = int(input())

# m번 반복
for _ in range(m):
    # n 입력 받기
    n = int(input())
    
    # 연산 횟수를 저장할 변수
    count = 0
    
    # n이 1이 될 때까지 반복
    while n != 1:
        # n이 짝수면 2로 나누고
        if n % 2 == 0:
            n = n // 2
        # n이 홀수면 3을 곱하고 1을 더한다
        else:
            n = n * 3 + 1
        # 연산 횟수 증가
        count += 1
    
    # 연산 횟수 출력
    print(count)