#include <stdio.h>
#include <string.h>

int find_substring(const char *input, const char *target) {
    int input_length = strlen(input);
    int target_length = strlen(target);

    // 입력 문자열의 길이와 목표 문자열의 길이를 비교하여
    // 목표 문자열이 입력 문자열에 포함될 수 있는지 확인
    for (int i = 0; i <= input_length - target_length; i++) {
        // 부분 문자열 비교
        if (strncmp(&input[i], target, target_length) == 0) {
            return i; // 부분 문자열의 시작 인덱스 반환
        }
    }
    return -1; // 부분 문자열이 존재하지 않을 경우
}

int main() {
    char input[9999]; // 최대 1000자 + 널 종료 문자
    char target[9999];

    // 입력 받기
    fgets(input, sizeof(input), stdin);
    fgets(target, sizeof(target), stdin);

    // 개행 문자 제거
    input[strcspn(input, "\n")] = 0;
    target[strcspn(target, "\n")] = 0;

    // 부분 문자열 찾기
    int index = find_substring(input, target);
    printf("%d\n", index);

    return 0;
}