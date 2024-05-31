# 입력 받기
n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 연속부분수열 여부 확인
def is_subsequence(A, B):
    for i in range(n1):
        # 수열 B의 첫 원소와 일치하는 수열 A의 원소를 찾음
        if A[i] == B[0]:
            # 수열 B의 모든 원소가 수열 A에 연속적으로 존재하는지 확인
            if A[i:i+len(B)] == B:
                return "Yes"
    return "No"

# 결과 출력
print(is_subsequence(A, B))