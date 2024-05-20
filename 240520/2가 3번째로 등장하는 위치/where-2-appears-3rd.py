n = int(input())
m = list(map(int, input().split()))
cnt = 0
i = 0

for i in range(n):

    if m[i] == 2:
        cnt += 1
    if cnt == 3:
        break

# cnt가 3에 도달했는지 확인
if cnt == 3:
    print(i+1)