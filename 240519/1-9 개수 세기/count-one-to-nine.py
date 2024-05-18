n = int(input())  # 사용자로부터 정수 n을 입력받습니다.
elements = list(map(int, input().split()))  # 공백으로 구분된 정수들을 입력받아 리스트로 변환합니다..


count_arr = [0] * 10

# 개수 세기

for i in elements:
    count_arr[i] += 1

# 개수 출력
for i in range(1,10):
    cnt = count_arr[i]
    print(cnt)