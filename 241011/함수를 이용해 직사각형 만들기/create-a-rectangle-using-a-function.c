#include <stdio.h>

void print_rect(int n, int m) {
    for (int i = 0; i < n; i++) { // 조건을 i < n으로 수정
        for (int j = 0; j < m; j++) { // m에 대한 반복 추가
            printf("1");
        }
        printf("\n"); // 각 행의 끝에서 줄 바꿈
    }
}

int main() {
    int n,m;

    scanf("%d,%d",&n,&m);
    print_rect(2, 3);
    return 0;
}