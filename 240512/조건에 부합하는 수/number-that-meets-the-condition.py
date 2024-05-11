a=int(input())
# for i in range(1,a+1):
#     if i%2!=0 and i%4==0:
#         if i //8%2!=0:
#             if i//7 >=4:
#                 sorted(print(i))a = int(input())

for i in range(1, a+1):
    # 1번 조건의 부정: 홀수이거나 4의 배수인 수
    condition1 = i % 2 != 0 or i % 4 == 0
    
    # 2번 조건의 부정: 8로 나눈 몫이 홀수인 수
    condition2 = (i // 8) % 2 != 0
    
    # 3번 조건의 부정: 7로 나눈 나머지가 4 이상인 수
    condition3 = i % 7 >= 4
    
    # 세 조건 중 하나라도 참이라면 출력
    if condition1 and condition2 and condition3:
        print(i, end=' ')