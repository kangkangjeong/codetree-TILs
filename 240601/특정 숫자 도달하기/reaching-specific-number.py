n=list(map(int,input().split()))
cnt=0
sum=0
for i in n:
    if i<250:
        cnt+=1
        sum+=i
    else:
        break
print(f'{sum} {(sum/cnt):.1f}')