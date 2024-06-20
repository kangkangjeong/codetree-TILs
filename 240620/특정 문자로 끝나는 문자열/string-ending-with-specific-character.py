a=[input()
for _ in range(10)]
for i in range(len(a)):
    if a[i][-1]==a[-1][-1]:
        print(a[i])
    else:
        None