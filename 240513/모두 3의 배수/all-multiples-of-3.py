# 입력 받기
numbers = [int(input()) for _ in range(5)]

# 3의 배수 판단
is_multiple_of_three = all(number % 3 == 0 for number in numbers)

# 출력
print(1 if is_multiple_of_three else 0)