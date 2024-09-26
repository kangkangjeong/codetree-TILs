#include <stdio.h>

int main() {
    int temp;
    scanf("%d", &temp);    // 포맷 문자열 수정
    if (temp < 0)
        printf("ice");
    else if (temp < 100)
        printf("water");
    else
        printf("vapor");

    return 0;
}