# 첫 줄에 정수 n을 입력받습니다.
n = int(input())
# 두 번째 줄에 n개의 정수를 입력받아 리스트로 변환합니다.
numbers = list(map(int, input().split()))

# 짝수만을 담을 리스트를 선언합니다.
even_numbers = []

# 입력받은 숫자들을 순회하며 짝수만을 찾아 even_numbers 리스트에 추가합니다.
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# even_numbers 리스트를 역순으로 출력합니다.
# *를 사용하여 리스트의 요소들을 공백으로 구분하여 출력합니다.
print(*even_numbers[::-1])