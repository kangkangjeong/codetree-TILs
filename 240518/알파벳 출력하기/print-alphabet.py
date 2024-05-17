n=int(input())
x=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(x),end='')
        if x>81:
            x=65
        else:
            x+=1
    print()