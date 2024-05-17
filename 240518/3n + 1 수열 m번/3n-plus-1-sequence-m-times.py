n=int(input())
for i in range(n):
    m=int(input())
    cnt=0
    while m!=1:
    
        if m%2==0:
            m=m/2
            cnt+=1
        elif m%2==1:
            m=m*3+1
            cnt+=1
    print(cnt)