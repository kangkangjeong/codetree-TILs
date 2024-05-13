# 나이들을 저장할 리스트 초기화
ages = []

# 무한 반복
while True:
    # 사용자로부터 나이 입력 받기
        age = int(input())
            
                # 나이가 20대가 아니면 반복 종료
        if age < 20 or age >= 30:
            break
                                
                                    # 나이가 20대이면 리스트에 추가
        ages.append(age)

                                        # 평균 계산 및 출력
                                        # sum(ages)는 ages 리스트의 모든 요소의 합, len(ages)는 리스트의 길이(요소의 개수)
if len(ages) > 0:
    average_age = sum(ages) / len(ages)
    print(f"{average_age:.2f}")
else:
    print("20대의 나이 정보가 없습니다.")