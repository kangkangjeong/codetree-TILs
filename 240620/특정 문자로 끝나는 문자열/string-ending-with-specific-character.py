a=[input()
for _ in range(10)]
b=input()
for i in range(len(a)):
    if a[i][-1]==b:
        print(a[i])
    else:
        None