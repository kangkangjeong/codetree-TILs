#include <stdio.h>

int main() {
    float num;  // num을 float 타입으로 변경

    printf("숫자를 입력하세요: ");
    scanf("%f", &num);  // %f로 수정

    if (num >= 1.0)
        printf("High\n");
    else if (num < 1.0 && num >= 0.5)  // 조건 수정
        printf("Middle\n");
    else
        printf("Low\n");

    return 0;
}