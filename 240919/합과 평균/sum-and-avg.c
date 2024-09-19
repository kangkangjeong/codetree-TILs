#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    
    int sum = a + b; // 합계 계산
    float average = sum / 2.0; // 평균 계산 (정확한 소수점 이하 유지)

    printf("%d %.1f\n", sum, average); // 결과 출력
    return 0;
}