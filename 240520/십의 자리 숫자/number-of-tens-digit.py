count_arr=[0]*10
int_list=list(map(int,input().split()))
for i in int_list:
    if i>10:
        count_arr[i//10]+=1
    if i==0:
        break
for j in range(1,10):
    print(f'{j} - {count_arr[j]}')