sum=0
for i in range(1,5):
    a_list=list(map(int,input().split()))
    for j in a_list[:i]:
        sum+=j
print(sum)