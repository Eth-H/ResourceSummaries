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
        //none:, -i: ignore case, -r/-R: recursive search - do/dont follow symlinks, -s: supress error msg, -v: search for lines without searchQuery
        //-n: line number, -a[numberOfLines]: return numberOfLines surrounding found results, -b: byte offset with output lines 
        //-E: use extended regular expression, can also use egrep, use if using any advanced RE patturns
        grep {}?... [searchquery] [filename]
        //EGs
            cat securityEventFile | grep -a[numberOfLines] [targetString]	
            grep fileName "b[ab]*" //ba... bb...

## edit files
    //blank: alphabetic order, -n: numeric order, -R: random order
    //-u: remove duplicate lines, -r: sort in reverse, -k [columnNum]: sort particular column
        sort {}...
    //remove duplicate lines, -c: get how many times the line was duplicated
    //-w [num]: max num chars to compare per line
        uniq
    //extract certain columns from file 
    //-d[delimiter]: EG ' '
    //-b: by bytes, -c: by num charl, -f: by fields
     //[-x]: up to x, [x-y]: range, [x-]: after x
        cut {} {} [fileName]?

    //join >1 files together line by line
        paste [fileOne] [fileTwo] ...
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

### insert txt at certain place
#### sed (stream editor)
    //substitution
        sed ‘s/term/replacement/flag’ [file]
        sed ‘s/y/Y/g’ [file]
        //special chars (file globbing chars) need to be escapped
        sed 's/and/\&/g;s/^I/You/g' [file]
    //print certain num lines
        sed -n 1,5p [file]
    sed '/^#\|^$/d' [file]
    //replace a line
        //note: sed -i is not posix standard
        sed '[targetLineNumber] cnewline [textToReplaceWith]' [fileName] 
        sed -i '[targetLineNumber]/.*/[replacementLine]/' file.txt		
        sed -i 'Ns/.*/replacement-line/' file.txt
        awk '{ if (NR == 4) print "different"; else print $0}' input_file.txt > output_file.txt
        awk 'NR==4 {$0="different"} 1' input_file.txt
        awk 'NR==4 {$0="different"} { print }' input_file.txt
            
            
### text editor 
    //Either will create file if it doesnt exist
        nano
            nano [filePath]
        vim
            //More powerful CLI text editor
                vim [filePath]
            //use i for insert/interactive mode, v for visual mode (select
stuff), esc to return to normal mode
            // :q quit with saved changes, :q! quit while you have unsaved changes, :wq save and quit


# to rm
//Time command
    time []

shell features 
    //change shell
        chsh {}
    History 
        //Show history
            history	
        //Delete history
            history -c
        //For a reverse-command-search use CTRL + R, then type in part of a previous command, CTRL + R again to go further back
        
        //Hide commands
            //Prefix each command with a 'space'
            //or
                set +o history
