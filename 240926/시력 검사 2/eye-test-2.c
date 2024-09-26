#include <stdio.h>

int main() {
    int num;
    scanf("%f",&num);
    if(num>=1.0)
        printf("High");
    else if(num>=0.5)
        printf("Middle");
    else
        printf("Low");
    return 0;
}