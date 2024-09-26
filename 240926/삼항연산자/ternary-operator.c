#include <stdio.h>

int main() {
    int choice;

    scanf("%d", &choice);

    // switch 문을 사용하여 선택된 작업 수행
    switch (choice/10) {
        case 10:
            printf("pass");
            break;

        default:
            printf("failure");
            break;
    }

    return 0;
}