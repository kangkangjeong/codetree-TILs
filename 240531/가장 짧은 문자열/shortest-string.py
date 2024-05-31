text_list=[]
for _ in range(3):
    text_list.append(input())

for i in range(3):
    if len(text_list[i])>len(text_list[0]):
        ma=len(text_list[i])
for j in range(3):
    if len(text_list[j])<len(text_list[0]):
        mi=len(text_list[j])
    else:
        mi=len(text_list[0])

print(ma-mi)