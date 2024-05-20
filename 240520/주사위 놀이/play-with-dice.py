dice_list=list(map(int,input().split()))
count_list=[0]*7
for element in dice_list:
    count_list[element]+=1
for i ,value in  enumerate(count_list):
    if i>0:

        print(f'{i} - {value}')