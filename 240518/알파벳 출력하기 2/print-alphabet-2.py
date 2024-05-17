n=int(input())
x=65
for i in range(n):
    for j in range(n):
        if i<=j:
            if x>89:
                x=65
                print(chr(x),end=' ')
                x+=1
            else:
                print(chr(x),end=' ')
                x+=1
        else:
            print(' ',end=' ')

    print()