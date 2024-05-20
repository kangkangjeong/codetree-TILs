list_arr=[]
count_arr=[0]*5
for _ in range(3):
    flue ,body_degree=input().split()
    body_degree=int(body_degree)
    if flue =='Y' and body_degree>=37:
        list_arr.append(1)
    elif flue =='N' and body_degree>=37:
        list_arr.append(2)
    elif flue =='Y' and body_degree<37:
        list_arr.append(3)
    elif flue =='N' and body_degree<37:
        list_arr.append(4)
for i in list_arr:
    count_arr[i]+=1
for j in range(1,5):
    print(count_arr[j],end=' ')
if count_arr[1]>=2:
    print('E')