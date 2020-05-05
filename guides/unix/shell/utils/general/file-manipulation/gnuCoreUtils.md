//some tools may behave differently on BSD based systems (generally more minimalistic)
#manage files and filesystem
## basic file operations
### list
    //List file directories
    //-l: Long form list of folders, -t: Sort by modification time, -a: Hidden files, -alt: Combination of previosu commands
        ls {} [specificPath]
    //list working directory
        pwd
    //change directories 
    //..: Back one, .:curretn directory, ~: home, /home/agent/Desktop: specific path
        cd {}
### edit
    move/rename
        //blank: no parameters, -n: Dont overwrite, -u: overwrite if timestamp is newer 
            mv {} [filePath] [targetFilePath]
    copy 
        //blank: no parameters, -r or -R: use recursive parameter to copy directories (and contents)
            cp {} [filePath] [filePath]	
    remove  
        //blank: no parameters, -r: recursive, allows to remove folders
            rm {} [filePath]
    make directory 
        mkdir [directoryPath]
        //Make multiple directories
            mkdir -p [folderName]/[subFolderName]/[subFolder2Name]
        //Set permissions
            mkdir -m 777 dirname

### view file
        cat 
            //print/concantonate text file/files contents to console
                cat filename
                cat filename1 filename2
        //Change amount of contents displayed
            //Gradually load program into memory
                less [filePath]	
                more [filePath]
            //-[x]: Output first x chars, -n [x] (same as -[x])
                head {} [file] 

            //-[x]: Output last x chars, -n [x], same as -[x]
                tail {} [file]
            //Output contents of file as it grows starting from last ten lines
                tail -f file
        strings 
            //Get all strings in a file
                strings [filePath]		

### advanced viewing
    compare directories/files
        //-q: Only report on differences, -r: recursive
            diff {}? [dir1] [dir2]
        //compare byte to byte 
            cmp

### search for files
    find 
        //-name:, can use wildcards in file name EG "*myfile*"
        //-mtime -[num]: find files in the last 30 days, -size +[num]M: find files   10 MB in size
        //-perm -[permissionsValuable], -user [user]
        find [searchDirectoryPath] {searchMethod}... [searchQuery]
        //EG Search entire file system and redirect errors to a certain file 
            find / -name "passwords" 2>  /dev/null
            find [path] {} {}?

    //get path of cmds
        whereis [cmd]
        which [cmd]
        //will also give alias
        type [cmd]

### create file 
        echo "[text]" > [newFilePath]
    //check if a file exists, if it doesnt create it
        touch [filename]	
    //tee
    //output to file and stdout
        echo "text" | tee [outputFileName]...

# file properties
    //read file headers/magic bytes
        file [filePath]
    //count num of lines, words and bytes in file 
        //-l -w -c: specify one
            wc {}?


# file manipulation
all cmds also operate on txt passed from stdin
## search file
    grep 
    //search for strs
        //none:, -i: ignore case, -r/-R: recursive search - do/dont follow symlinks, 
        //-A/-B/-C: lines before/after/both context
        //-v: search for lines without searchQuery
        //-s: supress error msg, 
        //-n: line number, -a[numberOfLines]: return numberOfLines surrounding found results, -b: byte offset with output lines 
        //-E/-G/-P: use extended/basic/perl regular expression, egrep/grep/pgrep
        grep {}?... [searchquery] [filename]
        //EGs
            cat securityEventFile | grep -a[numberOfLines] [targetString]	
            grep fileName "b[ab]*" //ba... bb...
    non-gnu
        rg //ripgrep
        ag //the silver searcher
## edit files
### manipulate systematically
    export LC_ALL=C # set locale to default, forces byte-wise sort order
        //EG  LC_ALL=C sort A B a b   LC_ALL=en_US sort a A b B
#### reorganise
    //sort
        //blank: alphabetic order, -n: numeric order, -h: human numeric (EG 2k 1G), -R: random order
        //-u: remove duplicate lines, -r: sort in reverse, -k [columnNum]: sort particular column
        //-t [fieldSep]: field separator (\t, \n)
            sort {}...
            //EG
                sort -k1,1 | sort -s -k2,2 #sort first by field 2, then by field 1
    //rm dupe lines
        //remove duplicate lines, -c: get how many times the line was duplicated
        //-w [num]: max num chars to compare per line
        //-u: only unique lines, -d: only print duplicated lines (one per dupe)
            uniq
    //advanced
        datamash
##### shuf
    write random perms of file/stdin to stdout
    //-r: allow for repated perms of files, -n [num]: max num generated vals
    //-i [num]-[num1]: gen range to be treated as inp lines
    shuf {}...
    //EG
        //shuffle lines of file
            shuf file
        //output 50 random numbers each in range 0-9
            shuf -r -n 50 -i 0-9
#### extract
    //extract certain columns from file 
    //-d[delimiter]: EG ' '
    //-b: by bytes, -c: by num charl, -f: by fields
     //[-x]: up to x, [x-y]: range, [x-]: after x
        cut {} {} [fileName]?
#### merge
    //join >1 files together line by line (by row or col)
        paste [fileOne] [fileTwo] ...
            //EG
                //file1: A    file2: C    file3 A C
                         B           D          B D
                paste file1 file2 > file3
        //paste but both lines must share a common field that is (sortable by sort)
        //only outputs lines with a matching value in that common field
            join
            //EG
                //file1: 1 A    file2: 1 C    file3 1 A C
                         2 B           2 B          2 B B
                                       3 A
                join file1 file2 > file3

        //convert set of chars into anouther
            -d: del chars in first set
            -c: complement (ignore) first set of characters
            -s: replace multiple adjacent occurances of first set with second
            -t: truncate first set, useful if first set > chars than second
                tr {}?... [charset1] [charset2]?
            //eg 
                //convert lowercase in a file to uppercase
                    cat sample.txt | tr 'a-z' 'A-Z'
                //use file globbing (regex) character classes
                    cat sample.txt | tr [:lower:] [:upper:]
                cat sample.txt | tr -d ‘is’
                echo “Phone number is 123456789” | tr -cd [:digit:] //del only non-numbers

#### split files contents
    //via size
        split
    //via ptn
        csplit
#### edit actual file size
    truncate #sparse files
    fallocate #ext4, xfs, btrfs and ocfs2 filesystems 



### text editor 
    //Either will create file if it doesnt exist
        nano
            nano [filePath]
        vim
            //More powerful CLI text editor
                vim [filePath]

## compare files
    //line by line
        comm
        diff
        sdiff //side by side diff

    vimdiff [file]{2,4} //compare and edit files
### use to patch source
    //apply diff file to original
        patch
    diffstat //diff summary
        //EG
            diff -r tree1 tree2 | diffstat


## advanced file parsing
sed and awk process files line by line in a pattern space buffer
### sed (stream editor)
restructure input via patturn substituions
### awk
programming lang to scan/process

# args stream editing
## xargs
    -L [max lines]: control how many items exe per line
    -P [maxParallel]: max num processes that can run simultaneously
    -I [replaceStr]: replace occurances of RS in initial-args with names read from stdin
    -I{}: 
    xargs {}
    //EGs
        find . -name '*.py' | xargs grep some_function
        cat hosts | xargs -I{} ssh root@{} hostname
