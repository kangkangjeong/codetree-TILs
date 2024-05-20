from collections import Counter

# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))

# 숫자 빈도 계산
frequency = Counter(numbers)

# 중복되지 않는 숫자 중 최댓값 찾기
unique_numbers = [num for num, count in frequency.items() if count == 1]

# 결과 출력
if unique_numbers:
    print(max(unique_numbers))
else:
    print(-1)