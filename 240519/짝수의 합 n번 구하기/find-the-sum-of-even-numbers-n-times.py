n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    sum_even = 0  # 변수명을 sum에서 sum_even으로 변경하여 내장 함수와의 충돌 방지
    for k in range(a, b+1):
        if k % 2 == 0:
            sum_even += k
    print(sum_even)  # 각 테스트 케이스마다 짝수의 합을 출력