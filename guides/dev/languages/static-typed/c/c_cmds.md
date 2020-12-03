# compile
## clang
    todo
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
    //pass a lib at runtime, EG ncurses
        gcc -o [fileName] fileName.c -lncurses
## MinGW cross-complier
compile for windows
    //setup
        sudo apt-get install mingw-w64
    //create 32 bit exe
        i686-w64-mingw32-gcc -o main32.exe main.c
    //create 64-bit Windows
        x86_64-w64-mingw32-gcc -o main64.exe main.c
