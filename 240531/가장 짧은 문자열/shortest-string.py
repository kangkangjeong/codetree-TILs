text_list = []
for _ in range(3):
    text_list.append(input())

# 초기값 설정 시 첫 번째 요소의 길이를 사용
ma = len(text_list[0])
mi = len(text_list[0])

for i in range(3):
    if len(text_list[i]) > ma:
        ma = len(text_list[i])
    if len(text_list[i]) < mi:
        mi = len(text_list[i])

print(ma - mi)