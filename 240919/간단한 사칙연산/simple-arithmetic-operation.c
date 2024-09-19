#include <stdio.h>

int main() {
    int a, b;  // 변수 선언

    // 두 정수를 입력받음
    scanf("%d %d", &a, &b);

    // 연산 결과 출력
    printf("%d\n", a + b);     // 덧셈
    printf("%d\n", a - b);     // 뺄셈
    printf("%d\n", a / b);   // 나눗셈 (정수 나눗셈)
    printf("%d\n", a % b);   // 나머지 연산

    return 0;
}