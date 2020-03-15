#include<stdio.h> 

int main(){
    int number = 50;
    int *p;
    p = &number;
    printf("%p\n", p);
    printf("%d\n", *p);
    return 0;
}
