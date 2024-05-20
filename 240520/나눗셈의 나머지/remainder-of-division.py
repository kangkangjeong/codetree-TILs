a,b=map(int,input().split())
cnt_list=[0]*10

while True:
    cnt_list[a%b]+=1
    a=a//b
    if a<=1:
        break
sum=0
for i in range(10):
    if cnt_list[i]>=1:
        sum+=cnt_list[i]**2
print(sum)