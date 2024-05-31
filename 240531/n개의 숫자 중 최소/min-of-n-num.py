n=int(input())
a_list=list(map(int,input().split()))
cnt=0
small=min(a_list)
for i in a_list:
    if i == small:
        cnt+=1
print(min(a_list),cnt)