# 입력된 날짜 정보를 받습니다.
input_date = input()

# 입력된 날짜 정보를 '-'를 기준으로 분리합니다.
mm, dd, yyyy = input_date.split('-')

# yyyy.mm.dd 형식으로 출력합니다.
print(f"{yyyy}.{mm}.{dd}")