#include <stdio.h>

int main() {
    // 변수 선언
    int a, b;

	// 입력
	scanf("%d %d", &a, &b);
	
	a += b;
	b += a;
    
    // 출력
	printf("%d %d", a, b);
    return 0;
}