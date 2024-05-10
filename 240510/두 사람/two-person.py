age1, sex1 = input().split()
age2, sex2 = input().split()
age1 = int(age1)
age2 = int(age2)

# 두 사람 중 한 사람이라도 19세 이상이며, 그 사람이 남자인 경우를 정확히 확인
if ((age1 >= 19 and sex1 == 'M') or (age2 >= 19 and sex2 == 'M')):
    print(1)
else:
    print(0)