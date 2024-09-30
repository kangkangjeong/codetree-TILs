#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);  // n의 주소를 전달해야 합니다.
    
    for (int i = 0; i < n; i++) {  // n에 따라 반복
        for (int j = 0; j < n; j++) {  // 5개의 '*' 출력
            printf("*");
        }
        printf("\n");  // 각 줄 끝에 줄바꿈 추가
    }

    return 0;
}