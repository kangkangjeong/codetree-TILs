a = list(map(str, input().split()))
for i in range(len(a)):
    if i % 2 == 1:
        print(a[i-1])