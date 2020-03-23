#include<stdio.h> 

int main(){
    char name[20];
    char wame[] = "dada";
    int arr[3] = {1, 1, 1, 1};
    int number = 50;
    int *p;
    p = &number;
    printf("%p\n", p);
    printf("%d\n", *p);
    return 0;
}
