
# terms
binary file
    non-text file computer file
    seq of bytes
    header magic signiture/number can be used to identify file format
obj file
    contains obj code and related data
    obj files can be statically or dynamically linked
    types
        Relocatable (can be combined to form a exe with other relocatable types)
        Executable: binary code/data, cna be copied into mem
        Shared: can load into mem and linked dynamically
execuable/exe
    file can be run
    statically linked: contains copied static libraries internally
    dynamically linked: references external shared libraries, linking occurs while running

libraries
    collections of obj files used when linking obj files
    external code that can be imported and used within a program
    static: bundle of relocatable object files , .a
    shared: bundle of globally accessible obj files in /usr/lib/* (dll on win)

obj code
    compiler product
    instructions in a computer language
        usuall machine code language
            binary

# format
ELF (Executable and Linkable Format)
    format for exe files, obj code, shared libraries, core dumps
    unix x86 binary format
    get data with readelf or objdump

a.out (assembler output)
    older format for exes, obj code, sometimes shared libraries

COFF (Common Object File Format)
    older format for exes, obj code, shared libraries
    basis for ms PE format
PE (Microsoft Windows Portable Executable)
    exes, obj code, DLLs
