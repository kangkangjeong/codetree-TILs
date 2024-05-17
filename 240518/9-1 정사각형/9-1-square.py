n = int(input())  # 사용자로부터 정수 n을 입력받음

current_number = 9  # 시작 숫자를 9로 설정
for i in range(n):  # n번 반복하여 n개의 줄을 출력
    for j in range(n):  # 각 줄마다 n개의 숫자를 출력
        print(current_number, end='')  # 현재 숫자를 출력하고 줄바꿈 없이 다음 숫자를 이어서 출력
        current_number -= 1  # 현재 숫자를 1 감소시킴
        if current_number < 1:  # 현재 숫자가 1보다 작아지면
            current_number = 9  # 현재 숫자를 9로 재설정
    print()  # 한 줄 출력 후 줄바꿈