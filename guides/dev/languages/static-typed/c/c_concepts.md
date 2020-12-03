# language
tokens: keywords, identifier, constants, strings, special symbols (EG [] {}), operators
## data types
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
            char a[10];
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

### strings
    declare
        char ch[10]={'j', 'a', 'v', 'a', 't', 'p', 'o', 'i', 'n', 't', '\0'};
        char ch[]="javatpoint";
        printf("char arr: %s\n String Literal: %s\n", ch, ch2);
    store str while newline is not encountered
        char s[20];
        printf("Enter the string?");
        scanf("%[^\n]s",s);
#### pointers with strings
    //a strings identifier (sI = "...") is the base address of the string and is treated as a const pointer internally
        //hence we dont need to use & when assigning to pointer or passing to scanf()
    //is good practice declare char pointers to point at strings (will auto point to first elem)
    //this allows us copy/change from the str, since we repoint the internal pointer to anouther string
        char s[11] = "javatpoint";
        char *p = s; // pointer p is pointing to string s
        printf("%s",p);
        p = "yeet"; //overwrite pointer to point to anouther string
        //can use *p to access addr and p to access "s"'s internal pointer to its val
    //good practice to use const char * to declare string that we dont intend to change, since "x"[0] = 'a' is illegal
        const char *my_str = "This is my very own string literal";
        //though use char foo[] if str resides in writeable memory and u intend to assign chars inplace
    //to print a pointer, cast it to void
        printf("%p\n", (void *) &a);
#### inp/oup
    #include<stdio.h>

    char s[30];
    //allows user to enter space separated strings
    gets(s);
    //same as gets(), but make sure inp is less that 30 bits to avoid buffer overflow
    fgets(s);

    #include <string.h>
    char ch[20]={'j', 'a', 'v', 'a', 't', 'p', 'o', 'i', 'n', 't', '\0'};
    //print string with newline, returns num of printed chars (including added newline)
        puts(ch);


    # c reverse str//length str (without ending \0 null char)
        strlen("we")
    //cp str
        //only way to change str inplace without changing each char
        char ch2[20];
        strcpy(ch2,ch);
        strncpy(ch2,ch,2); //cp only first 2 chars
    //concat strs, return result to first str
        char ch3[10]={'c', '\0'};
        strcat(ch,ch3);
    //compare str, return 0 if equal
        strcmp(str1,str2)
    //return reversed str
        strrev(ch)
    //return lowercase, uppercase str
        strlwr(ch)
        strupr(ch)
    //returns pointer to the first occurrence of 2nd param str within 1st param str
        char *sub;
        sub=strstr(str,"java");

## operators
### compare
    3 == 2; // => 0 (false)
    3 != 2; // => 1 (true)
    3 > 2; 3 < 2; 2 <= 2; 2 >= 2;
    comparisons dont chain (unlike python)
        0 < a < 2; //means (0 < a) < 2
        0 < a && a < 2;
### logic
    // Logic works on ints
    !3; // => 0 (Logical not)
    !0; // => 1
    1 && 1; // => 1 (Logical and)
    0 && 1; // => 0
    0 || 1; // => 1 (Logical or)
    0 || 0; // => 0
### ternary - see conditional
### increment/decrement
    j++; // Return j THEN increase j
    ++j; // Increase j THEN return j
### bitwise
    ~0x0F; // => 0xFFFFFFF0 (bitwise negation, "1's complement", EG 32-bit int)
    0x0F & 0xF0; // => 0x00 (AND)
    0x0F | 0xF0; // => 0xFF (OR)
    0x04 ^ 0x0F; // => 0x0B (XOR)
    0x01 << 1; // => 0x02 (left shift (by 1))
    0x02 >> 1; // => 0x01 (right shift (by 1))

    // be careful when shifting signed integers - the following are undefined:
    // - shifting into the sign bit of a signed integer (int a = 1 << 31)
    // - left-shifting a negative number (int a = -1 << 2)
    // - shifting by an offset which is >= the width of the type of the LHS:
    //   int a = 1 << 32; // UB if int is 32 bits wide

## var declaration and assignment
    int x = 10;
    int a=10,b=20;
    int b, c; b = c = 0;
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
    printf("%d\n", (char)100.0); //can cast a num <255 to a char

## functions
    can only return 1 value
    to pass var by ref pass the pointer

### using global vars
// if referring to external variables outside function, you should use the extern keyword.
int i = 0;
void testFunc() {
  extern int i; //i here is now using external variable i
}

// make external variables private to source file with static:
static int j = 0; //other files using testFunc2() cannot access variable j
void testFunc2() {
  extern int j;
}

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

    void printIntArray(int *arr, size_t size) {
        int i;
        for (i = 0; i < size; i++) {
            printf("arr[%d] is: %d\n", i, arr[i]);
        }
    }

### func pointers
invoke funcs, pass handlers (or callbacks)
as long as function signatures match, you can assign any function to the same pointer
    void str_reverse(char *str_in){
      char tmp;
      size_t ii = 0;
      size_t len = strlen(str_in); // `strlen()` is part of the c standard library
      for (ii = 0; ii < len / 2; ii++) { // in C99 you can directly declare type of `ii` here
        tmp = str_in[ii];
        str_in[ii] = str_in[len - ii - 1]; // ii-th char from end
        str_in[len - ii - 1] = tmp;
      }
    }

    void str_reverse_through_pointer(char *str_in) {
      // Define a function pointer variable, named f.
      void (*f)(char *); // Signature should exactly match the target function.
      f = &str_reverse; // Assign the address for the actual function (determined at run time)
      // f = str_reverse; would work as well - functions decay into pointers, similar to arrays
      (*f)(str_in); // Just calling the function through the pointer
      // f(str_in); // That's an alternative but equally valid syntax for calling it.
    }

    //function pointers are usually typedef'd for simplicity and readability
    typedef void (*my_fnp_type)(char *);
    my_fnp_type f;


## control structures
### conditionals (decision)
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

### loops
    for (x = 0; x <= 5; x++){
        printf("x is %d\n", x);
    }
    do{
        //code to be executed
    }while(condition);
    //EG
        int kk = 0;
          do {
            printf("%d, ", kk);
          } while (++kk < 10);
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
      out: puts("get outttt!!")

## lists
### array
    fixed length list
    //Same as char arrays, can only hold data type used to create it, cant increase size (is a set)
    char array[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'};
    puts(array[0])
    int arr[4][3]={{1,2,3},{2,3,4},{3,4,5},{4,5,6}};

    ways to return an arr from a function
        [return array from func](./code_examples/##raff)
    //2D arr, save inp to arr
        int arr[3][3],i,j;
        for (i=0;i<3;i++){
            for (j=0;j<3;j++){
                printf("Enter a[%d][%d]: ",i,j);
                scanf("%d",&arr[i][j]);
            }
        }
        printf("\n printing the elements ....\n");
        for(i=0;i<3;i++){
            printf("\n");
            for (j=0;j<3;j++){
                printf("%d\t",arr[i][j]);
            }


## input
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
## files
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
## pointers and memory
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
        // * is used to declare a pointer, and to dereference it (retieve val at the mem addrs pointed to)
        int number = 50;
        //declare
            //must intialise with a mem location to point to
            //var of type pointer that points to mem addr of int var
                int *p = &number;
                //or
                int *p; p=&number;
        //can access mem addrs val with *p (dereference it) (unless declaring *p), or mem addr itself with p
            printf("Value of p variable is %d \n",*p); //50
            printf("Address of p variable is %p \n",p); //0x2014...
        //reset
            //can reset pointer mem addr
            //can also reset the current pointed to mem addrs val (via the dereferencing pointer)
                *p = 60 //now number = 60
    //can declare pointers to point at strings (without &)
        //if we do *p is the address and p is the value
        //see #strings/pointers with strings

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
        /*
            a[i] = *(p+i)
            the compiler often decays/converts an array expression from N-element arr of T to pointer to T, then it sets the expression val to the addr of the arrs first elem
            EG when passing the arr or assigning it to a pointer, but not when using &arr
        */

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
    uses heap, mem not freed unless you free it //avoid mem leaks
    malloc()
        //allocates single block of requested memory, return null if none avaliable
        //does not initialise block with any value;
        EG see dangling pointer case 1
    calloc()
        //allocates multiple block of requested memory, return null if none avaliable
        //initialise blocks with 0s;
        ptr=(int*)calloc(n,sizeof(int));  //memory allocated using calloc
        [code #mem alocation #calloc](./code_examples.md/#calloc-eg)
        //no way to track length of dynamically allocated arr in c
            //use a var to keep track
            size_t size = 10;
            int *my_arr = calloc(size, sizeof(int));
            // Add an element to the array
            size++;
            my_arr = realloc(my_arr, sizeof(int) * size);
            if (my_arr == NULL) {
                //Remember to check for realloc failure!
                return
            }
            my_arr[10] = 5;
            free(my_arr)

    realloc()
        //reallocates the memory occupied by malloc() or calloc() functions.
        ptr=realloc(ptr, new-size)
    free()	frees the dynamically allocated memory.
        free(ptr)

# maths func
    ceil(num): rounds up to >= int (though still stored as decimal)
    floor(num): rounds down to <= int (though still stored as decimal)
    sqrt(num): returns the square root
    pow(base, exponent): returns the power
    abs(num): returns the absolute value

    #include <math.h>
    printf("\n%f",ceil(3.6)); //4.000000
    printf("\n%f",floor(3.6)); //3.000000
    printf("\n%f",sqrt(7)); //2.645751
    printf("\n%f",pow(2,4)); //16.000000
    printf("\n%d",abs(-12)); //12

# struct
    store multiple attributes of an entity that have different data types
    sizeof(contents) != struct size as theres padding between members
    keyword -> tag -> fields/members
    //ways to declare
        //1, need to declare var in main func, can declare struct many times
        struct employee {
            int id;
            char name[50];
            float salary;
        };
        struct employee e1, e2;
        //2 struct declared inplace, use if num struct vars fixed
        struct employee {
            int id;
            char name[50];
            float salary;
        }e1,e2;
    //access members
        e1.id //member/dot operator
        e1->id //structure pointer operator
            int areaptr(const employee *e1)
            {
              return e1->id * e1->salary;
            }

    //give alias name to exisitng var
        typedef unsigned int unit;
        uint a = 10;

        //shorten struct name
            struct student{
                char name[20];
                int age;
            };
            typedef struct student stud;
            stud s1, s2;
    //arr of structs
            struct student st[5];


## nested struct
    //separate
        struct Date{
           int dd;
           int mm;
           int yyyy;
        };
        struct Employee{
           int id;
           char name[20];
           struct Date doj;
        }emp1;
    //embedded, can't be used in multiple data structures
        struct Employee{
            int id;
            char name[20];
            struct Date{
                int dd;
                int mm;
                int yyyy;
            }doj;
        }emp1;

## union
    only one field can occupy mem, so a unions instance size = its largest mem
    if anouther field is changed, already assigned fields will get garabge vals
    union employee{
        int id;
        char name[50];
        float salary;
    };

# file handling
    Creation, open, read, overwrite, del file
    file modes
        open txt files in mode
            r read, w write, a append
            r+ read and write
            w+ read and write
            a+ read and write
        open binary files in mode
            rb read, wb write, ab append
            rb+	read and write
            wb+	read and write
            ab+	read and write
    FILE* fopen(const char *filename, const char *mode)
        //opens new/existing file into buffer (as a stream)
        FILE *fp;
        fp = fopen("file_handle.c","r");
    int fprintf(FILE *stream, const char *format [, argument, ...])
        //write char set into file, accepts format string
        fprintf(fp, "Hello file by fprintf...\n")
    int fscanf(FILE *stream, const char *format [, argument, ...])
        //read char set, return EOF at EOF, accepts format specifier
        fp = fopen("file.txt", "r");
        while(fscanf(fp, "%s", buff)!=EOF){printf("%s ", buff );}
    int fputs(const char *s, FILE *stream)
        //write line of chars to file, dont accept fs but quicker at plain strs
        fputs("hello c programming",fp);
    char* fgets(char *s, int n, FILE *stream)
        //read line of chars, return EOF at EOF
        printf("%s",fgets(text,200,fp));
    int fputc(int c, FILE *stream)
        //writes a char
        fputc('a',fp);//writing single character into file
    int fgetc(FILE *stream)
        //read a char
        ch = fgetc (fp); //Each character of the file is read and stored in the character file, returns EOF at EOF
    fputw()	writes an integer to file
    fgetw()	reads an integer from file
    fclose(FILE *fp) //closes the file
    int fseek(FILE *stream, long int offset, int whence)
        //sets the file pointer to specified offset
        //whences: SEEK_SET (from file start), SEEK_CUR and SEEK_END
        fseek( fp, 7, SEEK_SET );
    long int ftell(FILE *stream)
        returns current file position
        pos = ftell(fp);
    rewind()
        //sets the file pointer to the beginning of the file
        rewind(fp);
    void rewind(FILE *stream)
        //move file pointer to start of stream
            rewind(fp);

# c preprocessor directives
    c micro processor transforms code before compiler
    preprocessor directives, #preprocessorDirectives
    #include
        paste code of file into given file, ignores \ and // within fn
        <fileName> //look for dir with system-header files (/usr/include)
        "fileName" //look in current dir for user-defined files
    #define
        define macro
    #undef
        undefine a defined macro
        #define number 15
        int square=number*number;
        #undef number
        #define ADD(a, b) ((a) + (b))
    #ifdef, #ifndef
        #ifndef MACRO
            //successful code
            #define macro
        #else
            //else code
        #endif
        //stop header being defined too many times, eg circle dependency

    //evaluate defined macros
    #if, #else, #elif, #endif
    #error
        stop compilation if found
        #error err msg
    #pragma
        provide additional info to compiler
        different compilers can provide different usage of #pragma directive
            #pragma startup
                Before the execution of main(), the function specified in pragma is needed to run.
            #pragma exit
                Before the end of program, the function specified in pragma is needed to run.
            #pragma warn
                Used to hide the warning messages.
            #pragma GCC dependency
                Checks the dates of current and other file. If other file is recent, it shows a warning message.
            #pragma GCC system_header
                It treats the code of current file as if it came from system header.
            #pragma GCC poison
                Used to block an identifier from the program.

## macros
    allows for macros, where code segments are replaced by a macros val
    obj like macros
        identifier replaced by val
        //EG repersent numeric constant
            #define PI 3.14
    function like macros
        #define MIN(a,b) ((a)<(b)?(a):(b))
    predefined macros
        _DATE_	represents current date in "MMM DD YYYY" format
        _TIME_	represents current time in "HH:MM:SS" format
        _FILE_	represents current file name
        _LINE_	represents current line number
        _STDC_	It is defined as 1 when compiler complies with the ANSI standard

# cli args
    #include <stdio.h>
    void main(int argc, char *argv[] )  {
       printf("Program name is: %s\n", argv[0]);
       if(argc < 2){
          printf("No argument passed through command line.\n");
       }
       else{
          printf("First argument is: %s\n", argv[1]);
       }
    }

# theory
## expressions
    arithmetic expressions
        bidmas
        EGs
            int/int
                3/2 = 1
            int/float
                6/2.0 = 3.0
    relational expressions
        x%2 == 0, a!=b
    logical
        x > 10 || y <11
        !(x>10) && (y==2)
    conditional
        return 1 if true, otherwise 0
        if, if else, else
        ternary
            exp1 ? exp2 : exp3
            status = (age>22) ? 'M': 'U';
## data segments
    vars, func, data structures allocated mem in data segment
### Data Area
    permanent memory area, stores all static and external variables
### Code Area
    memory area which can only be accessed by the function pointers. The size of the code area is fixed
### Heap Area
    the heap area is used to store the data structures which are created by using dynamic memory allocation. The size of the heap area is variable and depends upon the free space in the memory
### Stack Area
    has two parts: initialize and non-initialize. Initialize variables are given priority than non-initialize variables

        automatic, constant vars
        local vars of the default storage class
        func params and return value

        stack area is the temporary memory area as the variables stored in the stack area are deleted whenever the program reaches out of scope.

# progam flow
source -(preprocessor)> expanded source -(compiler)> assembly -(assembler)> obj code -(linker)> exe code -(loader)> mem
    preprocessor
        convert directives to respective vals
    linker
        links to the library (header files)

# share code between files
share datatypes and structures between files for consistency
define in headers
    // structs and typedefs
    typedef struct Node
    {
        int val;
        struct Node *next;
    } Node;

    // enumerations
    enum traffic_light_state {GREEN, YELLOW, RED};

    /* function prototypes */
    /* bad practice to define the function in the header Define in a c file */
    Node createLinkedList(int *vals, int len);

    /* other definitions should be left to a c source file */
    /* Excessive includes/definitions should not be contained in */
    /* a header file but instead put into separate headers or a C file.          */

    #endif /* End of the if precompiler directive. */
