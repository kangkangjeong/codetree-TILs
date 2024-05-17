# 정수 N 입력 받기
N = int(input())

# N부터 1까지 반복하여 줄을 출력
for i in range(N, 0, -1):
    # i부터 N까지의 숫자를 공백을 두고 출력
    for j in range(i, N+1):
        print(j, end=' ')
    # 한 줄 출력 후 줄바꿈
    print()