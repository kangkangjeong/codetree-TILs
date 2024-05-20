n = int(input())
m = list(map(int, input().split()))
cnt = 0
i = 0

for i in range(n):
    if cnt == 3:
        break
    if m[i] == 2:
        cnt += 1

# cnt가 3에 도달했는지 확인
if cnt == 3:
    print(i)
else:
    print("2가 3번 존재하지 않습니다.")