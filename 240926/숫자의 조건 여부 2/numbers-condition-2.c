#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);

    if (a == 5) {
        printf("A\n");
    } else if (a % 2 == 0) {  // 비교 연산자는 == 사용해야 합니다.
        printf("B\n");
    } else {
        printf("");
    }

    return 0;
}