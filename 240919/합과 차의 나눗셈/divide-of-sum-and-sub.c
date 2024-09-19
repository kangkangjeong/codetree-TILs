#include <stdio.h>

int main() {
    // 변수 선언 및 입력
    int a, b;
    scanf("%d %d", &a, &b);
    
    printf("%.2lf\n", (double)(a + b) / (a - b));
    return 0;
}