import math

gcd = math.gcd(1920, 2880)

def has_common_divisor(a, b):
    gcd = 960  # 1,920과 2,880의 최대공약수
    for i in range(1, gcd+1):
        if gcd % i == 0:  # i가 960의 약수인 경우
            if a <= i <= b:  # i가 주어진 범위 안에 있는지 확인
                return 1  # 공약수가 존재
    return 0  # 공약수가 존재하지 않음

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
print(has_common_divisor(a, b))