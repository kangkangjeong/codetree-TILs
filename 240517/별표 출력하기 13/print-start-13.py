n=int(input())
for i in range(1,(n+1)*2):
    if i%2==0:
        for j in range(i//2):
        
            print("*",end=' ')
    elif i%2==1:
        for j in range((n-i//2),0,-1):
            print('*',end=' ')
    print()