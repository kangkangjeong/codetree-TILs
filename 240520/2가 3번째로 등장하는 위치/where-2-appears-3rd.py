n=int(input())
m=list(map(int,input().split()))
cnt=0
for i in range(n):
    if cnt==3:
        break
    if m[i]==2:
        cnt+=1

print(i)