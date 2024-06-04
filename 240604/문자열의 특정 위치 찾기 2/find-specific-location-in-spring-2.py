strings=["apple", "banana", "grape", "blueberry", "orange"]
# 사용자로부터 문자를 입력받습니다.
char = input()
# 조건을 만족하는 문자열을 저장할 리스트를 초기화합니다.
matching_strings = []

# 각 문자열에 대해 세 번째나 네 번째 문자가 주어진 문자와 일치하는지 확인합니다.
for s in strings:
    if (len(s) >= 3 and s[2] == char) or (len(s) >= 4 and s[3] == char):
        matching_strings.append(s)

# 조건을 만족하는 문자열들을 출력합니다.
for s in matching_strings:
    print(s)

# 조건을 만족하는 문자열의 개수를 출력합니다.
print(len(matching_strings))