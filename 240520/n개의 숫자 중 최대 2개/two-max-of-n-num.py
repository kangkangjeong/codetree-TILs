n=int(input())
num_list=list(map(int,input().split()))
num_list.sort(reverse= True)
print(num_list[0],num_list[1])