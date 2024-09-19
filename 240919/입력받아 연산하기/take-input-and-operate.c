#include <stdio.h>

int main() {
    // 변수 선언
    int a, b;

	// 입력
	scanf("%d %d", &a, &b);
	
	a += 87;
	b %= 10;
    
    // 출력
	printf("%d\n%d", a, b);
    return 0;
}