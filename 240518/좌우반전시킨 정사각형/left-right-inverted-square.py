n = int(input())  # 사용자로부터 정수 n 입력 받기

for i in range(1, n+1):  # 행을 1부터 n까지 반복
    for j in range(n, 0, -1):  # 열을 n부터 1까지 역순으로 반복
        print(i * j, end=' ')  # 각 요소를 계산하여 출력 (행 번호 * 열 번호)
    print()  # 한 행이 끝날 때마다 줄바꿈