n=int(input())
for i in range(1,n+1): 
    if i % 2 == 0:
        for j in range(1,i+1):
            print("*",end=' ')
        print()
    else:
        print("*")