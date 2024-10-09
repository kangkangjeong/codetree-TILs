#include <stdio.h>

void print10star(); // 함수 프로토타입 선언
void printstar();   // 함수 프로토타입 선언

int main() {
    printstar();
    return 0;
}

void print10star() {
    for (int i = 0; i < 10; i++) {
        printf("*");
    }
    printf("\n"); // 줄 바꿈 추가
}

void printstar() {
    for (int i = 0; i < 5; i++) {
        print10star(); // 10개의 별을 출력하는 함수 호출
    }
}