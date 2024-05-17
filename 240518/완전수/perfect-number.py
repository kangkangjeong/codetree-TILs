start,end=map(int,input().split())
div_list=[]
def div(n):
    sum=0
    global div_list
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        div_list.append(n)
for i in range(start,end+1):
    div(i)
print(len(div_list))