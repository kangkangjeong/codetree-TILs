n = int(input())

for i in range(n):
    for j in range(n):
        # 첫 번째 라인, 마지막 라인, 첫 번째 컬럼, 마지막 컬럼, 대각선 위치에 있는 경우 별을 출력합니다.
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i > j:
            print('*', end=' ')
        else: # 그 외의 경우 공백을 출력합니다.
            print(' ', end=' ')
    print() # 각 라인이 끝날 때마다 새로운 라인으로 넘어갑니다.