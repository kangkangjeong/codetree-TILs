a1, a2 = map(int, input().split())
a_list = [a1, a2]  # a1과 a2를 a_list에 추가

# 첫 두 항이 이미 리스트에 있으므로, 8번만 더 반복하여 총 10개의 항을 만듭니다.
for i in range(8):
    a3 = a_list[-2] * 2 + a_list[-1]  # 마지막 두 항을 이용해 다음 항을 계산
    a_list.append(a3)  # 계산된 항을 리스트에 추가

for i in a_list:
    print(i,end=' ')  # 생성된 수열 출력