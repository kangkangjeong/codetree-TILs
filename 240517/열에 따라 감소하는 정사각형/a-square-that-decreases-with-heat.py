n = int(input())
for i in range(n):
    print(' '.join(str(x) for x in range(n, 0, -1)))