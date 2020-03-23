# recursion
    per each recurisive call
        creates a new cp of mtd in mem-> mtd returns data -> cp is removed from the mem
        separate stack maintained at each call to store func contents, stack destroyed after vale returned

        complexity in resolving and tracking the calls vals
            so we need to maintain the stack and track the vals of the vars defined in the stack
                do so via stack tracing

## factorial
    #include <stdio.h>  
    int fact (int);  
    int main(){  
        int n,f;  
        printf("Enter the number whose factorial you want to calculate?");  
        scanf("%d",&n);  
        f = fact(n);  
        printf("factorial = %d",f);  
    }  
    int fact(int n){  
        if (n==0){  
            return 0;  
        }  
        else if (n == 1){  
            return 1;  
        }  
        else{  
            return n*fact(n-1);  
        }  
    }  

## fibonnaci
    #include<stdio.h>  
    int fibonacci(int);  
    void main (){  
        int n,f;  
        printf("Enter the value of n?");  
        scanf("%d",&n);  
        f = fibonacci(n);  
        printf("%d",f);  
    }  
    int fibonacci (int n){  
        if (n==0){  
            return 0;  
        }  
        else if (n == 1){  
            return 1;   
        }  
        else{  
            return fibonacci(n-1)+fibonacci(n-2);  
        }  
    } 
# arr
## raff
//ways to return arr from func (memory management example)
    //return pointer pointing to arr (wrong way)
    //getarray() returns a var arr (local variable)
        //the arr var is allocated within getarray()'s stack frame. so when program control comes back to main() and getarray()'s stack frame is freed the memory location doesnt exist (its been de-allocated)
        //when the illegal memory location is returned it causes a segmentation fault
        #include <stdio.h>  
        int *getarray(){  
            int arr[5];  
            printf("Enter the elements in an array : ");  
            for(int i=0;i<5;i++){  
                scanf("%d", &arr[i]);  
            }  
            return arr;  
        }  
        int main(){  
          int *n;  
          n=getarray();  
          printf("\nElements of array are :");  
          for(int i=0;i<5;i++){  
                printf("%d", n[i]);  
          }  
          return 0;  
        }  
    //pass array which is to be returned as a parameter to the function
        #include <stdio.h>  
        int *getarray(int *a){  
            printf("Enter the elements in an array : ");  
            for(int i=0;i<5;i++){  
                scanf("%d", &a[i]);  
            }  
            return a;  
        }  
        int main(){  
          int *n;  
          int a[5];  
          n=getarray(a);  
          printf("\nElements of array are :");  
          for(int i=0;i<5;i++){  
                printf("%d", n[i]);  
            }  
            return 0;  
        }  
    //Returning array using malloc() function (dynamic array)
        #include <stdio.h>  
        #include<malloc.h>  
        int *getarray(){  
            int size;  
            printf("Enter the size of the array : ");  
            scanf("%d",&size);  
            int *p= malloc(sizeof(size));  
            printf("\nEnter the elements in an array");  
            for(int i=0;i<size;i++){  
                scanf("%d",&p[i]);  
            }  
            return p;  
        }  
        int main(){  
           int *ptr;  
           ptr=getarray();  
           int length=sizeof(*ptr);  
           printf("Elements that you have entered are : ");  
           for(int i=0;ptr[i]!='\0';i++){  
              printf("%d ", ptr[i]);  
            }  
          return 0;  
        }  
    //Using Static Variable
        #include <stdio.h>  
        int *getarray(){  
          static int arr[7];  
          printf("Enter the elements in an array : ");  
          for(int i=0;i<7;i++){  
              scanf("%d",&arr[i]);  
          }  
          return arr;  
        }  
        int main(){  
          int *ptr;  
          ptr=getarray();  
          printf("\nElements that you have entered are :");  
          for(int i=0;i<7;i++){  
              printf("%d ", ptr[i]);  
          }  
        }  
    // Using Structure
        #include <stdio.h>  
        #include<malloc.h>  
        struct array{  
            int arr[8];  
        };  
        //returns struct of type array
        struct array getarray(){  
            struct array y;  
            printf("Enter the elements in an array : ");  
            for(int i=0;i<8;i++){  
                scanf("%d",&y.arr[i]);  
            }  
            return y;  
        }  
        int main(){  
          struct array x=getarray();  
          printf("Elements that you have entered are :");  
          for(int i=0;x.arr[i]!='\0';i++){  
              printf("%d ", x.arr[i]);  
          }  
            return 0;  
        }  
# pointers
    //swap two vars without a third
        #include<stdio.h>  
        int main(){  
        int a=10,b=20,*p1=&a,*p2=&b;  
          
        printf("Before swap: *p1=%d *p2=%d",*p1,*p2);  
        *p1=*p1+*p2;  
        *p2=*p1-*p2;  
        *p1=*p1-*p2;  
        printf("\nAfter swap: *p1=%d *p2=%d",*p1,*p2);  
          
        return 0;  
        }  

# mem allocation
    //pass memory location to a func expecting a pointer
    #include <stdio.h>
    //doStuff function expects a pointer to an integer value
    void doStuff(int *stuff){
        //Access the data at the pointer
        *stuff = 1337;
        printf("Within the doStuff() function, the variable stuff has the value: %d\n\n", *stuff);
    }
    int main() {
        int stuff = 42;
        //stuffs memory addr passed
        doStuff(&stuff);
        //stuff value changed despite no return value
        return(0);
    }
## calloc eg
    #include<stdio.h>  
    #include<stdlib.h>  
    int main(){  
     int n,i,*ptr,sum=0;    
        printf("Enter number of elements: ");    
        scanf("%d",&n);    
        ptr=(int*)calloc(n,sizeof(int));  //memory allocated using calloc    
        if(ptr==NULL){    
            printf("Sorry! unable to allocate memory");    
            exit(0);    
        }    
        printf("Enter elements of array: ");    
        for(i=0;i<n;++i){    
            scanf("%d",ptr+i);    
            sum+=*(ptr+i);    
        }    
        printf("Sum=%d",sum);    
        free(ptr);    
    return 0;  
    }    
## malloc eg
    //Save stuff to the heap, it exists until you call free() on it 
        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>
        #include <time.h>
        int main() {
            // This program generates a random number between 0 and 19.
            // Creates a random number 0 to 19, then it creates a character array in memory on the heap 
            // big enough for that number of characters
            srand (time(NULL));
            int r = rand() % 20;
            printf("Going to save %d 'A's into memory this time!\n", r);
            // Create space for 'chars' number of characters + 1 byte on the heap
            // The extra byte is for the string line terminator which is a 0x00 or a null byte
            char *string = malloc((sizeof(char) * r) + 1);
            // For loop to add 'r' number of A's to the address at the string variable on the heap
            int i;
            for (i = 0; i < r; i++) {
                // The strcat function concatenates two strings together.
                // with parameters: result destination, string to add to destination
                strcat(string, "A");
            }
            puts(string);
            //Free heap memory when it is no longer needed, dont forget as it can lead to memory leaks
            free(string);
            return(0);
        }
## malloc eg2    
    //Return a string, use the heap to pass by reference 
        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>
        #include <time.h>
        char *getStr(int chars) {
            // Create space for 'chars' number of characters + 1 byte on the heap
            // The extra byte is for the string line terminator which is a 0x00 or a null byte
            char *string = malloc((sizeof(char) * chars) + 1);
            // For loop to add 'chars' number of A's to the address at the string variable on the heap
            int i;
            for (i = 0; i < chars; i++) {
                strcat(string, "A");
            }
            return(string);
        }
        int main(){
            // This program generates a random number between 0 and 19.
            // Then it creates a character array in memory on the heap big enough for
            // That random number of characters.
            // Generate a random number between 0 and 19
            srand (time(NULL));
            int r = rand() % 20;
            printf("Going to save %d 'A's into memory this time!\n", r);
            char *res = getStr(r);
            puts(res);
            free(res);
            return(0);
        }

# struct
    struct student{
        int rollno;    
        char name[10];    
    };    
    int main(){    
        int i;    
        struct student st[5];    
        printf("Enter Records of 5 students");    
        for(i=0;i<5;i++){    
            printf("\nEnter Rollno:");    
            scanf("%d",&st[i].rollno);    
            printf("\nEnter Name:");    
            scanf("%s",&st[i].name);    
        }
    }

## nested struct
    struct address{
        char city[20];  
        int pin;  
        char phone[14];  
    };  
    struct employee  
    {  
        char name[20];  
        struct address add;  
    };  
    void main (){
        struct employee emp;  
        scanf("%s %s %d %s",emp.name,emp.add.city, &emp.add.pin, emp.add.phone);  
        printf("name: %s\nCity: %s\nPincode: %d\nPhone: %s",emp.name,emp.add.city,emp.add.pin,emp.add.phone);  
    }
## union eg
    #include <stdio.h>  
    #include <string.h>  
    union employee{
        int id;    
        char name[50];    
    }e1;  //declaring e1 variable for union  
    int main(){  
       //store first employee information  
       e1.id=101;  
       strcpy(e1.name, "Sonoo Jaiswal");//copying string into char array  
       //printing first employee information  
       printf( "employee 1 id : %d\n", e1.id); //1869508435
       printf( "employee 1 name : %s\n", e1.name); //Sonoo Jaiswal
       return 0;  
    }  

# file
    //open and read line by line
    #include;
    void main(){
        FILE *fp; // file pointer
        char ch; 
        fp = fopen("file_handle.c","r");
        while (1){
            ch = fgetc ( fp ); //Each character of the file is read and stored in the character file.  
            if ( ch == EOF )
            break;
            printf("%c",ch);
        }
        fclose (fp );
    }
    //write data at specific location
    #include <stdio.h>
    void main(){  
       FILE *fp;  
      
       fp = fopen("myfile.txt","w+");  
       fputs("This is javatpoint", fp);  
        
       fseek( fp, 7, SEEK_SET );  
       fputs("sonoo jaiswal", fp);  
       fclose(fp);  
    }  
    //ftell
        fp = fopen("file.txt", "r");  
        fseek(fp, 0, SEEK_END);  
        length = ftell(fp);  
        fclose(fp);  

# c preprocessor
## macros
    #include <stdio.h>  
    #define MIN(a,b) ((a)<(b)?(a):(b))  
    void main() {  
       printf("Minimum between 10 and 20 is: %d\n", MIN(10,20));    
    } 

    #ifndef EG
        #include <stdio.h>  
        #include <conio.h>  
        #define INPUT  
        void main() {  
            int a=0;  
            #ifndef INPUT  
                a=2;  
            #else  
                printf("Enter a:");  
                scanf("%d", &a);  
            #endif         
            printf("Value of a: %d\n", a);  
        }  
    evalute vale of defined vals
        #include <stdio.h>  
        #include <conio.h>  
        #define NUMBER 0  
        void main() {  
            #if (NUMBER==0)  
                printf("Value of Number is: %d",NUMBER);  
            #endif         
        }  
    err
        #include<stdio.h>  
        #ifndef __MATH_H  
        #error First include then compile  
        #else  
        void main(){  
            float a;  
            a=sqrt(7);  
            printf("%f",a);  
        }  
        #endif  
## pragma
    start exit
        #include<stdio.h>  
        #include<conio.h>  
        void func() ;  
        #pragma startup func  
        #pragma exit func  
          
        void main(){  
            printf("\nI am in main");  
        }  
          
        void func(){  
            printf("\nI am in func");  
        }  
    I am in func
    I am in main
    I am in func

