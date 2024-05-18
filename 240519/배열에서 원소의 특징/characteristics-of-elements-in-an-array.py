number=list(map(int,input().split()))
for i in range(1,len(number)) :
    if number[i] % 3==0:
        print(number[i-1])
        break