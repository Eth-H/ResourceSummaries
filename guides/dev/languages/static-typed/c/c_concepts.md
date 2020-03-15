# language
tokens: keywords, identifier, constants, strings, special symbols (EG [] {}), operators
## Data Types
    types
        Basic: int, char, float, double
        Derived: array, pointer, structure, union
        Enumeration: enum
        Void: void

    sizes
        unsigned
            1 byte 0 to 255, 2 byte 0 to 65,535, 4 byte 0 to 4,294,967,295, 8 byte 2^64, 10 byte 2^80
        signed
            1 byte -128 to 127, 2 byte −32,768 to 32,767, 4 byte -2,147,483,648 to 2,147,483,647, 8 byte -2^63 to (2^64)-1, 10 byte -2^79 to (2^79)-1
        EG A signed 32 bit integer -32,767 to +32,767, unsigned: 0 to 65535, "^16 = 65535 so 16 bits in size"
    literals
        Integer
            int: 2by integer value, short: 2by short integer value, long: 4by long integer value
            //prefix with val to refer to other base numbering system
                //octal 020
                //hex 0x20
            //suffix
                //unsigned 20u
                //long size 20l
        Float
            float: 4by Single-precision floating point value.
            double: 8by Double-precision floating point value.
            long double: 10by
            decimal form
                normal EG 10.5
            exponential form
                EG +1e23, -9e2, +2e-25   
        Char
            Integer type that is always 1 byte large, can hold characters
             Use '' for a char and "" for a char array
            char a = 'a';
        String (char arr)
            char a[] = "hello";
        bool
            true = 1, false = 0
            bool x=false; 
### format specifiers
    string used in the formatted input and output functions 
    %d or %i 	signed integer
        %u 	unsigned integer
        %o octal unsigned integer (has prefixed 0 value)
        %x hexadecimal unsigned integer (has prefixed 0x value), alphabetically chars shown lowercase
        %hd short signed integer  
            %hu short unsigned integer
        %ld long signed integer
            %lu long unsigned integer
    %X same as %x but alphabetically chars shown uppercase
    %f decimal floating-point values, by default shows 6 values after '.'.
    %e/%E scientific notation, Mantissa or Exponent
    %g decimal floating-point values, uses the fixed precision (num vals after 0 = exact inp)
    %p address in a hexadecimal form
    %c unsigned character
    %s strings (expects Char Array terminated with a null byte which is hexadecimal 0x00)
    EG
        //use stdio.h for all input/output related functions
        #include <stdio.h>
        int main(){
            short aShort = 42;
            unsigned short anUnsignedShort = 42;
            printf("aShort contains: %hd and is size: %lu\n", aShort, sizeof(aShort));
            printf("anUnsignedShort contains: %hu and is size: %lu\n", anUnsignedShort, sizeof(anUnsignedShort));
            //specify precision
                float x=12.2;  
                printf("%.2f", x);  
            char character = 'A';
            printf("character is: %c\n", character);
            printf("character is also decimal: %d\n", character);
            printf("character is also hexadecimal: %x\n", character);

            char string[] = "Hello, World!";
            printf("A string is just an array of characters, for example: %s\n", string);
        
        #Increment: 
        anInt++
        anInt--
        
        return(0);
    }
    
    //string insertion via method
        string body = string.Format("My ID is {0}", ID)
### escape sequences
    seq of characters that doesn't represent itself when used inside string literal or character
    \a	Alarm or Beep
    \b	Backspace
    \f	Form Feed
    \n	New Line
    \r	Carriage Return
    \t	Tab (Horizontal), \v  Vertical Tab
    \\	Backslash
    \'	Single Quote, \"  Double Quote
    \?	Question Mark
    \nnn	octal number, \xhh	hexadecimal number
    \0	Null

## var declaration and assignment
    int x = 10;
    int a=10,b=20;
    const float PI=3.14;  
    //other assignment symbols
    = += -= *= /= %=>>= <<= &= ^= |=
### storage classes
    summary (local scopes global if declared in main scope)
    SC      Storage Place	Default Val	Scope	Lifetime
    auto 	RAM             Garbage Val	Local	Within function
    extern	RAM             Zero	    Global	entire main program maybe declared anywhere in the program
    static	RAM             Zero	    Local	entire main program, retains value between multiple functions calls
    register         Register Garbage  Value	Local	Within the function
#### automatic
    allocated mem automatically at runtime
    auto int x = 10;
    int x = 0; //auto flag applied automatically
#### static
    doesnt belong to container its declared in
    EG
        static global var //declared ontop of program
        static func //lifetime throughout program
        static local vars //value kept between mtd calls
        static member variables (class fields)//accessed by all instances of a class rather than a specific instance
        static mtd (class func) //same as static class fields
    static int y=10;
#### register
    ask cpu to store var in its registers if it has room
    cant dereference (cant use &), but can store pointers
    quick access
    cant store static vars
    register int a = 0;
#### external
    tell the compiler that the var defined as extern is declared with an external linkage elsewhere in the program.
        no mem allocated
    can only initialise globally
    can be declared many times but can only be initialised once
        extern int x=10;
### type casting
    float f=(float) 9/4;


## Functions
### library func
    func declared in library header files
    include header files to use them

    common header files
        stdio.h	standard inp/output
        conio.h	console inp/output
        string.h string related Eg: gets(), puts()
        stdlib.h general Eg: malloc(), calloc(), exit()
        math.h math operations Eg: sqrt(), pow()
        time.h time-related
        ctype.h	character handling
        stdarg.h Variable argument
        signal.h signal handling
        setjmp.h jump
        locale.h locale functions
        errno.h	error handling
        assert.h diagnostics functions.


### user-defined func

    #include <stdio.h>
    int addStuff(int valueA, int valueB) {
        puts("The addStuff function was called");
        return(valueA + valueB);
    }
    int main() {
        int result = addStuff(5, 10);
        printf("The answer is: %d\n", result);
        //Return 0 if the program run successfully or 1 if unsuccessfully
        return(0)
    }
## Conditionals (decision)
    int r = rand() % 20;
    if (r < 5) {
        puts("r is less than 5");
    } else if (r > 15) {
        puts("r is greater than 15");
    } else {
        puts("r is not less than 5 or greater than 15.");
    }

    switch(number){    
        case 10:    
            printf("number is equals to 10"); break;    
        case 50:    
            printf("number is equal to 50"); break;    
        default:    
        printf("number is not equal to 10, 50 or 100");    
    }

## Loops
    for (x = 0; x <= 5; x++){
        printf("x is %d\n", x);			
    }		
    do{  
        //code to be executed  
    }while(condition);  
    while(condition){  
        //code to be executed  
    } 

    //goto, jump to label, usefull to jump out of nested loops
      int i, j, k;    
      for(i=0;i<10;i++){  
        for(j=0;j<5;j++){  
            printf("%d %d %d\n",i,j);  
            if(j == 3){goto out;}  
        }  
      }
      out: 

## Lists
### array
    fixed length list
    //Same as char arrays, can only hold data type used to create it, cant increase size (is a set)
    char array[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'};
    puts(array[0])	
    int arr[4][3]={{1,2,3},{2,3,4},{3,4,5},{4,5,6}};
    
    ways to return an arr from a function
        [return array from func](./code_examples/##raff)
## Input
    //Array stores 20 bytes of data
    char data[20];
    puts("Enter some data here: ");
    //Points to the space on the memory stack
    scanf("%s", &data);
    printf("You entered: \n%s\n", data);
    //User can exploit with buffer overflow, since the can enter >20 bytes
    
    //More secure, max bytes to read, adds a newline
    fgets(data, sizeof data, stdin);
    printf("You entered: \n%s", data);
    
    //If newline is cut off add before printing result
    if (strlen(data) > 0){
        if (data[strlen(data) - 1] != '\n') {
            data[strlen(data) - 1] = '\n';
        }
    }	
    
    //Command line arguments
        int main(int argc, char *argv[]) {
            int i;
            for (i = 0; i < argc; i++) {
                printf("Arg %d: %s\n", i, argv[i]);
            }
            return(0);
        }
## Files
    #include <stdio.h>
    #include <string.h>
    int main() {
        char data[20];
        FILE *file = fopen("test.txt", "r");
        fgets(data, sizeof data, file);
        if (strlen(data) > 0){
            if (data[strlen(data) - 1] != '\n') {
                data[strlen(data) - 1] = '\n';
            }
        }
        printf("The file contains: \n%s", data);
            fclose(file);
        return(0);
    }
## Pointers and memory
### memory allocation contex
    Saving a variable process: the program asks the kernel for some space in memory -> kernel provides a memory address -> data is stored into memory at that location.
    stack and heap (memory types)
        when a variable is declared, that memory will exist on the stack, though the program needs to know exactly 
         how much memory to allocate during compiling, so a max no. of characters is needed
        memory on the heap can be allocated dynamically during runtime, so user can type any number of characters
    pass by value and ref
        Because each func has its own stack frame, vars on the stack cant be accessed outside of their func 
         so vars are passed as a copy (value)
        To pass by reference (the actual variable) you chave to pass a vars mem addr (and store it to a pointer)

### basic
    pointer: memory address that points to the contents of a var
    pointer size is 8 bits
    pointer to the mem address of a variable (where it is stored)
    //refer to vars mem addr
        &varName
    // use a pointer
        int number = 50;
        //must intialise with a mem location to point to
        //var of type pointer that points to mem addr of int var
        int *p = &number; //or could use int *p; p=&number;
        //can access mem addrs val with *p (dereference it), or mem addr itself with p
        printf("Value of p variable is %d \n",*p);
        printf("Address of p variable is %p \n",p);
        //can reset pointer mem addr
        //can also reset the current pointed to mem addrs val (via the dereferencing pointer)
        *p = 60 //now number = 60

### examples
    int* x; int *x; //equal, but first expresses var as type pointer
           
    passing pointers to func
        * as a type modifier
            int i //declares an int.
            int* p //declares a pointer to an int.

            void foo(int i) declares a function taking an int (by value, i.e. as a copy).
            void foo(int* p) declares a function taking a pointer to an int.
        * and & as operators
    
            foo(i) calls foo(int i). The parameter is passed as a copy.
            foo(*p) dereferences the int pointer p and calls foo(int i) with the int pointed to by p.
            foo(&i) takes the address of the int i and calls foo(int* i) with that address.
    pointer to arr
        int arr[10];  
        int *p[10]=&arr; // Variable p of type pointer is pointing to the address of an integer array arr. 

        int a[10] = {100, 206, 300, 409, 509, 601}; //Line 1  
        //use pointer arithmetic to access arr items via mem
        int *p[] = {a, a+1, a+2, a+3, a+4, a+5}; //Line 2  
    pointer to func
        void foo (int);  
        void (*p)(int) = &foo; // Pointer p is pointing to the address of a function  
        //call 
        (*p)(number);

        int (*p)(int (*)[2], int (*)void)) //pointer to such function with first param pointer to a one-dimensional array of int[2] and second param as the pointer to a func with param void and return type int.
    double pointer
        int **p; // pointer to a pointer which is pointing to an int
    pointer arithmetic
        //new_address= current_address + i * size_of(data type)  
        int number=50;
        int *p; p=&number;
        p=p+1; //increments p (&number) by 4 bytes

        //some invalid operations can cause an address which leads to illegal pointer
            EG address + address
    arr of functions
        //pointer pointing to an array which contains the pointers to the functions
        #include<stdio.h>  
        int show();  
        int showadd(int);  
        int (*arr[3])();  
        int (*(*ptr)[3])();  
        int main (){  
            int result1;  
            arr[0] = show;  
            arr[1] = showadd;  
            ptr = &arr;  
            result1 = (**ptr)();  
            printf("printing the value returned by show : %d",result1);  
            (*(*ptr+1))(result1);  
        }  
        int show(){  
            int a = 65;  
            return a++;  
        }  
        int showadd(int b){  
            printf("\nAdding 90 to the value returned by show: %d",b+90);  
        }

    dangling pointer causes
    //obj deleted/de-allocated from mem and pointer unmodified
        //free() used
            int *ptr=(int *)malloc(sizeof(int));  
            int a=560;  
            ptr=&a;  
            free(ptr);
            //assign null to stop 
            ptr=NULL;
        //var falls out of scope
            char *str;  
                {  
                    char a = ?A?;  
                    str = &a;  
                }  
                // a falls out of scope   
        //Function call
            //when program control returns to main(), int *fun()'s stack framw containing y is deleted
            #include <stdio.h>  
            int *fun(){  
                int y=10;  
                return &y;  
            }
            int main(){
                int *p=fun();
                printf("%d", *p);  
                return 0;  
            }  
    //constant
        //const pointer, addr cannot be changed
        int* const ptr;  
        //pointer to const, val cannot be changed  
        const int* ptr;  
        //constant pointer to a constant, neither can be changed
        const int* const ptr;  
    //void pointer
        //generic pointer that can point to any data type, highly reuseable
        //malloc() and calloc() return void pointers, so can cast and assign
            int *x = (int*)malloc(sizeof(int));
        //cannot dereference void pointer, cast first
            int a=90;  
            void *ptr;  
            ptr=&a;  
            printf("Value which is pointed by ptr pointer : %d",*(int*)ptr);  

### dynamic memory allocation
    allows to allocate mem at run time and increase during execution
    uses heap, mem not freed unless you free it
    malloc()	
        //allocates single block of requested memory, return null if none avaliable
        //does not initialise block with any value;
        EG see dangling pointer case 1
    calloc()	
        //allocates multiple block of requested memory, return null if none avaliable
        //initialise blocks with 0s;
        ptr=(int*)calloc(n,sizeof(int));  //memory allocated using calloc
        [code #mem alocation #calloc](./code_examples.md/#calloc-eg)
    realloc()	
        //reallocates the memory occupied by malloc() or calloc() functions.
        ptr=realloc(ptr, new-size)  
    free()	frees the dynamically allocated memory.    
        free(ptr)

    
    
    /* So the methods to pass actual varaibles between functions are (pass by reference):			
    You could create a variable in the main function and pass a pointer to the variable into the doStuff function, 
     which will then modify the data at that memory address and then return. This would work because the variable 
     was created in the main() function, which hasn't returned yet.
     You could allocate memory on the heap, and return a pointer to that memory address. 
     Memory on the heap exists until you call free() on it, no matter where it was created, so even if you 
     allocate the memory inside the doStuff() function it will still exist even when the doStuff() function returns.
    */
