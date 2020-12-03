# terms/context
    lib paths
        where global c libs are stored
        /usr/lib /usr/local/lib

# linking
https://www.cs-fundamentals.com/c-programming/static-and-dynamic-linking-in-c
linking: collecting and combining multiple object files in order to create a single executable
## static linking
    performed at compile time as the last step
    lib routines copied into exe image
    adv: faster, portable
    dis-adv: larger, less flexible
    EG manually link local lib
```c
    
        add.h
            int add(int, int);
        add.c
            int add(int quant1, int quant2){
              return(quant1 + quant2);
            } 
        addDemp.c
            #include <add.h>
            #include <stdio.h>
            int main(){
              int x= 10, y = 20;
              printf("\n%d + %d = %d", x, y, add(x, y));
              return 0;
            }
```
        // compile addDemo to obj code using header files in current dir
        gcc -I . -c addDemo.c
        // compile to obj code, no header files needed
        gcc -c add.c
        //link obj files
        gcc -o addDemo add.o addDemo.o
    //create static lib
        sub.c
            int sub(int quant1, int quant2){
              return (quant1 - quant2);
            }
        heymath.h //header for the libararies contents
            int add(int, int); //adds two integers
            int sub(int, int); //subtracts second integer from first
        //create static lib
        ar rs libheymath.a add.o sub.o
        //can now use #include <heymath.h> in addDemo() for hence add() and sub()
        //dont have to link add.o and sub.o individually
            //manually
            gcc -o addDemo addDemo.o libheymath.a
            //or, heymath lib from the cwd (-I for .a)
            gcc -o addDemo -L . addDemo.o -lheymath
            //if libraries placed within a global lib folder (installed to system), dont need to specify -L
            gcc -o addDemo addDemo.o -lheymath

## dynamic linking
    performed when program loaded into mem and exe by loader or at app runtime
    shareable lib name placed in exe image, exe and lib linked in mem
    adv: share lib saving space, programs get to use updated libs without relinking
    create shared lib
        with heymath.h add.c sub.c
        //compile with position independant code generation
            //-fPIC for multi-platform -fpic for platform dependant
            //-Wall checks for common errs
            gcc -Wall -fPIC -c add.c
            gcc -Wall -fPIC -c sub.c
        //create shared lib
            gcc -shared -o libheymath.so add.o sub.o
        // to use a shared lib it must be installed (via a lib folder)
            mv to /use/lib
            ldconfig
        // can compile
            gcc -o addDemo addDemo.o libheymath.so
            gcc -o addDemo addDemo.o -lheymath
    //list linked shared libs
        ldd [exe]

## other gcc flags
-Wall -Wextra -Werror -O2 //verbose err options
-std=c99  //c/c++ lang standard
-pedantic //stick to iso c/c++ standard
