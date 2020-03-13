# shell
## gcc (gnu compiler)
compile for linux
    //setup
        //extra packages for 32 bit compling
            sudo apt-get install libc6-dev
            sudo apt-get install gcc-multilib
            sudo apt-get install libc6-dev:i386
    //Run a C program via compling it into an ELF
        gcc -o [fileName] fileName.c
    //Specify processor arcitechure
        gcc -m32 -o [fileName] fileName.c
    //pass a library at runtime, EG ncurses	
        gcc -o [fileName] fileName.c -lncurses
## MinGW cross-complier
compile for windows
    //setup
        sudo apt-get install mingw-w64
    //create 32 bit exe
        i686-w64-mingw32-gcc -o main32.exe main.c
    //create 64-bit Windows
        x86_64-w64-mingw32-gcc -o main64.exe main.c

# language
    Data Types
        Integer
            //int: An integer value, short: A short integer value, long: A long integer value
            //These can be unsigend or signed (can be a -ve value, but the most signifcant bit is a sign bit (so 2^31))
             //EG A signed 32 bit integer -32,767 to +32,767, unsigned: 0 to 65535, "^16 = 65535 so 16 bits in size"
             //A short is similar to an integer, A signed long: -2,147,483,647 to +2,147,483,647, unsigned: 0 to 4,294,967,295		 
        Float
            //Float: Single-precision floating point value.
            //Double: Double-precision floating point value.
        Char
            //Integer type that is always 1 byte large, can hold characters
            //For a string make an array of characters
            // Use '' for a char and "" for a char array
        //use stdio.h for all input/output related functions
        #include <stdio.h>
        int main(){
            int anInt = 42;
            long aLong = 42;
            short aShort = 42;
            unsigned int anUnsignedInt = 42;
            unsigned long anUnsignedLong = 42;
            unsigned short anUnsignedShort = 42;
            printf("anInt contains: %d and is size: %lu\n", anInt, sizeof(anInt));
            printf("aLong contains: %ld and is size: %lu\n", aLong, sizeof(aLong));
            printf("aShort contains: %hd and is size: %lu\n", aShort, sizeof(aShort));
            printf("anUnsignedInt contains: %u and is size: %lu\n", anUnsignedInt, sizeof(anUnsignedInt));
            printf("anUnsignedLong contains: %lu and is size: %lu\n", anUnsignedLong, sizeof(anUnsignedLong));
            printf("anUnsignedShort contains: %hu and is size: %lu\n", anUnsignedShort, sizeof(anUnsignedShort));
            
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
        //String specifiers summary: %d is for an int, %ld is for a long, %hd is for a short, 
        // %u is for an unsigned int, %lu is for an unsigned long, %hu is for an unsigned short
        // %c is for a character, %x is for hexadecimal
       // %s is for a string (expects Char Array terminated with a null byte which is hexadecimal 0x00)
        
        //string insertion via method
            string body = string.Format("My ID is {0}", ID)

    Functions
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
    Conditionals
        int r = rand() % 20;
        if (r < 5) {
            puts("r is less than 5");
        } else if (r > 15) {
            puts("r is greater than 15");
        } else {
            puts("r is not less than 5 or greater than 15.");
        }
    Loops
        for (x = 0; x <= 5; x++){
            printf("x is %d\n", x);			
        }		
    Lists
        //Same as char arrays, can only hold data type used to create it, cant increase size (is a set)
        char array[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'};
        puts(array[0])	
    Input
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
        
        Command line arguments
            int main(int argc, char *argv[]) {
                int i;
                for (i = 0; i < argc; i++) {
                    printf("Arg %d: %s\n", i, argv[i]);
                }
                return(0);
            }
    Files
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
    Pointers and memory
        //when a variable is declared, that memory will exist on the stack, though the program needs to know exactly 
        // how much memory to allocate during compiling, so a max no. of characters is needed
        //memory on the heap can be allocated dynamically during runtime, so user can type any number of characters
        
        //A pointer is just a memory address that points to the contents of a variable
        //Saving a variable process: the program asks the kernel for some space in memory -> kernel provides a memory address -> data is stored into memory at that location.
        //Access memeory address
        &variableName
        //Because each function has its own stack frame, variables on the stack cant be accessed outside of their function. 
        // This means passed variables are just a copy (passing by reference)
        
        //To pass by reference (the actual variable) you can pass the memory address 
        #include <stdio.h>
        //doStuff function expects a pointer to an integer value
        void doStuff(int * stuff){
            //Access the data at the pointer
            *stuff = 1337;
            printf("Within the doStuff() function, the variable stuff has the value: %d\n\n", *stuff);
        }
        int main() {
            int stuff = 42;
            printf("Within the main function, before doStuff is called, the variable stuff has the value: %d\n\n", stuff);
            doStuff(&stuff);
            printf("Within the main function, after doStuff is called, the variable stuff has the value %d\n\n", stuff);
            return(0);
        }
        
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
        /* So the methods to pass actual varaibles between functions are (pass by reference):			
        You could create a variable in the main function and pass a pointer to the variable into the doStuff function, 
         which will then modify the data at that memory address and then return. This would work because the variable 
         was created in the main() function, which hasn't returned yet.
         You could allocate memory on the heap, and return a pointer to that memory address. 
         Memory on the heap exists until you call free() on it, no matter where it was created, so even if you 
         allocate the memory inside the doStuff() function it will still exist even when the doStuff() function returns.
        */
