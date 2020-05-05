//this document explains how to use bash
//page 50

# terminology
	data streams
		// stdin (0)  = input
		// stdout (1) = output
        // stderr (2) = err
        //there are 6 other streams that are generally unused
	exit/return status
		//all cmds return a exit/return status, where 0 is successful and other values match a specific error code, in a script the last cmd run determines the scripts exit status

# config
## bash files automatically run
    on login
        ~/.bash_profile or .profile
    on new shell
        ~/.bashrc
## max cmd line arg length
    grep ARG_MAX /usr/include/linux/limits.h
        #define ARG_MAX 131072 
    find ./ -name '*' -print0 | xargs -0 -n 10 rm #bypass

## change default shell
    chsh [shellName]

## within scripts
    aliases
        alias ll="ls -latr"
        alias fzfed='fzfed() { $EDITOR "$(find -type f 2>/dev/null | fzf)" ;}; fzfed'
    debugging
        set -x 
        set -v (logs raw inp)
        set -e abort on errs
        set -u to detect unset variable usages
        set -o pipefail,    to abort on errors within pipes
        trap use on exit or err
        set +o history //disable history, can also prefix cmds with a space

        set -euo pipefail
        trap "echo 'error: Script failed: see failed cmd above'" ERR
## env variables
    $PWD, $PATH, $USER, $HOME
    //output all env
        env
    //last cmds exit status
		$?
    //current running script PPID, script name
			$$, $0

# run something in a subshell
    ./scriptName
    (cd /some/other/dir && other-cmd)
    //since run in a subshell, any dir changes wont persistent in the parent shell

# argument passing
	In the linux kernel one word arguments are passed with -, multiple single letter arguments can be chained
	A word argument needs a -- prefix
	//BSD syntax uses no dashes before a parameter
# shortcuts
	up arrow: show the previous cmd
    ctrl-r: search cmd history (type to search, press ctrl-r to cycle matches)
    //jobs
        ctrl-z: stops the current cmd, resume with fg/bg
        ctrl-c: halts the current cmd, cancel the current operation and/or start with a fresh new line
    //flexible mv/del/manipulate (similar to vim/emacs)
        ctrl-w: to delete the last word
        ctrl-u: cut from cursor to line start
        ctrl-k: cut from cursor to line end
        ctrl + y: paste from the special clipboard (ctrl + u and ctrl + k save to)
        alt-b, alt-f: to move by word
        ctrl-a/ctrl-e: to move cursor to beginning/end of line
        ctrl-t: swap the two characters before the cursor
	ctrl-l: clear the screen
    alt-.: cycles previous args
    alt-*: expands a glob
    alt-#: add a # at the beginning and enter it as a comment (or ctrl-a, #, enter), you can then return to it later via cmd history
	ctrl-d: log out of current session, similar to exit
	esc-.: insert the last argument of the previous cmd on the fly
    if set: export EDITOR=vim
        ctrl-x, ctrl-e: open current cmd in an editor for multi-line editing. Or in vi style, escape-v.

    //alternative to Ctrl keybindings allowing vi modes/keys
        set -o vi

# syntax
    quotes
        eliminate whitespace
        ""
        '' //characters lose ther meaning within
    file globbing
        mechanisum similar to regex using symbols like wildcards
        file globs expand to match files
        ls .*
        [fu]*
        *.*f*u

    Search text (regex)
        //use for ed, sed, awk, grep, find, vi, ...
        cmd ... " regexQuery... " ...
        // generally the same as javascript
        //but some features might not work in bash or other apps
            //PCRE expressions
                \d \D \s \S \w \W            
                //if so use posix class equlivants    
                    [[:digit:]], [^[:digit:]], [[:space:]], [^[:space:]], [_[:alnum:]], and [^_[:alnum:]]
                    [[:digit:]], [^[:digit:]], [:punct:], [:alpha:]
                        [_[:alnum:]] ([:alpha:]+[:digit:],[0-9A-Za-z])
                        [:print:] ([:alpha:]+[:print:])
                    [[:space:]], [:blank:], , [:xdigit:] (hex)

            //non-greedy matching 
                greedy chars: *, +, ?, {n,m} {n,}
                greedy: match string upto entire seach query
                non-greedy: match string upto any char from search query
                non-greedy:  
                //EG
                    m/^(.*)ab/
                    .* will backtrack to find regex patturns following it 
                    so it will match up till it finds an ab or ba
                    follow with ? to change to none greedy
                        m/^(.*?)ab/
                        .* will match up till it finds an a or b
            //non-capturing parentheses (grouping assertions)
                (?:...), group but dont capture
                    /(?:a)/ - match a but not captured for replacement
            //lookarounds (lookahead/lookbehind assertions)
                (?<=before) (?!after)
                ?=, ?!, ?<=, ?<!.
	Operators>
			
			//|, Passes the stdout of a previous cmd to the stdin of the next one
			//-, redirection from/to stdin or stdout
				//EG pipe to the end of a cmd
				bunzip2 -c linux-2.6.16.tar.bz2 | tar xvf -
		// \, escape, give characters their literal meaning
			echo "The book cost \$7.98."
			//special escaped characheters
				\n //newline, \r //return, \t //tab, \v //vertical tab, \b //backspace
				\a //alert
	
            //Use "" to use something in that exact way (escape its alt meaning), '' act as a stronger version, EG '' is needed to escape the escape character '\'  
                //EG to find an exact word
                    find -name "exactFileName"
            Line formatting>
                //Run two cmds on a line,
                    echo "Hello"; echo "World"				
                //Write a cmd on two lines (escapes whitespace)
                    echo "Hello "\
                    "World"	
                //Run cmd in the background, freeing up terminal to run cmds
                    echo "Hello" &			
				
		operators used mostly in scripting>
			//comma
				//link series of arithemtic equations (only the last one is returned)
					let "t2 = ((a = 9, 15 / 3))"
				//concatenate strings
					/{,usr/}bin/
			//null cmd
				:
			//!
				not 
			//?
				//in (())	construct can act as c-style trinary operator		
				//condition?result-if-true:result-if-false
					(( var0 = var1<98?9:21 ))
			//()
				//cmd group, acts as a subshell that cant be read by the rest of the script	
					(a=hello; echo $a)
				//declare array
					Array=(element1 element2 element3)
				//integer expansion, expand and evaluate contained integer expression
					(($a + $b))
				
			//{}
				//extended brace expansion
					echo {a..z} # a b c d e f g h i j k l m n o p q r s t u v w x y z
					echo {0..3} # 0 1 2 3
				//anonymous function, but with globally visible variables
					{ local a; a=123; }
					
	Path>
        ./   ..  //current/parentdir
		//Run via path starting from the root folder 
        //extract filename from path
            basename [path]
        //extract last dir from path
            dirname [path]
		//tidle, ~, home direcotory
			//~+, current working direcotry (pwd, $PWD)
			//=~, previous working direcotry ($OLDPWD)
        //filenames with whitespace
            "$FOO"
            locate -0 pattern | xargs -0 ls -al
            find / -print0 -type d | xargs -0 ls -al
            IFS=$'\n'  prepare to iterate filenames with white space


	//custom
		variableName=value variableName2 = value2
		$value, ${value}
		numbers="1 2 3"
		//remove variable value
			unset variableName
		//declare variable and perform arithemtic caluclation
			let "uninitialized += 5"
		
//job control
    ctrl z
    //%[jobNum]: 
    bg {}?
    fg {}?
    cmd & 
    //list jobs
        jobs -l 
    //kill proc, %[job num]:, [job PID]:,
        kill {}
        //sure kill
        kill -KILL
    //show info about logged in users and their processes 
        w

//history
    history
    //specific cmd
    ![historyNumber]
    //last cmd
        !!
    //last cmd args, *: all args, ^: 1st arg, $: 2nd arg
        !{}
    //Delete history
        history -c

//permissions	
    //user, group, other
    //read, write, exe
    //get info
        groups

    //change
        //who can change: root can change owner, owner can change group owner if within previous group owner
        //who, u | g | o | a: user, same group, other, all users 
         //operator, + | - | =: add, remove, exact permissions
          //permissions, r: read, w: write, x: execute 
        chmod {}{}{}
        //or use numbers, num1=user, num2=group, num3=other, 1=x, 2=w, 4=r 
            chmod 755



# Scripting
	//Tell system what compilier/interpretor to use
		//sha-bang  (#! is a two byte magic number) followed by path to the interpretor program for that script
			//EGs
			#!/bin/sh
			#!/bin/bash
			#!/usr/bin/perl
			#!/usr/bin/tcl
			#!/bin/sed -f
			#!/usr/awk -f
			//since the sha-bang is always run first, below causes a self-deleting script
				#!/bin/rm
## use script
    //Make that text file an executable, can give more permissions if needed
        chmod +x myscript.sh
    //run it
        ./myscript.sh
    //move to a directory listed in path for global use
        /usr/local/bin
			
## script env variables
   $[envVar] , ${[envVar} //same as above
    $0=shell script name
    $1=arg0, $2=arg1, $3... = arg...
    $* //all args
    $# //num of args passed 
		
		//move value from one positional parameter to anouther	
			$1 <--- $2
## iteration
    for item in items; do 
        [cmdInvolvingItem, $item]; 
    done
    while true; do  [thing] [if statement to terminate]
## decision
    [test] [expression]
    //return 0 if expr true, 1 if false
    
    //test construct, compares args and returns 1/0 relative to
exit status
        \[ expr \]
            ! expr //oposite
            //-a: true if both true (&), -o: true if either true (|)
                expr = expr1 

            //=, !=
                str {} str1 
            //-eq: a=b, -ne: a!=b, -gt: a>b, -lt: a<b, -ge: a>=b
                num {} num1 

            //-r: readable, -w: writeable, -x: executable, -f: is file, -d: is dir 
            //-e: true if exists, -L: true if symbolic link, 
                {} file 
            //-nt: file 1 newer than file 2, -ot: older
                file1 {} file2
            //-z: string empty, -n: not empty               
                {} string
            
    //extended test
        //[[ ... ]]  		
        //acts more like scripting languages
    //arithemetic constructs
        //(( ... ))
        //returns exit status relative to arithemtic espressions expand to a non-zero value (=0 ES=1, <0 >0 = ES=0) 
        //EGs
            (( 0 && 1 )) //$? = 1
            //return result directly with $ (without assigning a variable)
                echo $(( 7 + 7 ))
            //nest and assign variables half way through
                echo $(( myvar = 7 + $(( vartwo = 4 + 4 )) )
        //let ... assigns the result of an equation to a value, however the exit status acts similarly to (( ... )), returns exit status relative to result (=0 ES=1, <0 >0 ES=0)
            //EG
                let x=-1 ; echo x=$x \$?=$? // x=-1 $?=0
    //implement constructs
        //if else block
            if [exp]; then 
                ...
            elif [exp]; then
                ...
            else
                ...
            fi
        //case
            case "var" in 
            'val')
                ...;    
                ;;   
            'val1 | Val1')
                ...;    
                ;;   
            *)
                ...;
                ;;
            esac

## functions
    functionName(){
        #print passed parameter
        echo $1
    }
    #function call
    functionName "parameter"
    #pass function as parameter, with its paramters
        function x()      { echo "x(): Passed $1 and $2";  }
        function around() { echo before; "$@"; echo after; }
        around x 1st 2nd
    
# edit streams		
    //cmd stdout to cmd stdin
        [cmdOne] | [cmdTwo]
        //EG
            cmd | less – Allows the scrolling of the bash cmd window using Shift + Up Arrow and Shift + Down Arrow
    // redirect stodut to stdin and to a file         
        ls [dirPath] | tee [file]
    //inject cmd stdout where ever u want
        cmd `cmd1`
        cmd $(cmd1)
    // use < > to redirect stdout
        //redirect stdout to file, >: overite, >>: append
            cmd > file
        //redirect stdout to a cmds arg, <, <<
 to a file
            
            cmd < cmd1
            //EG
                diff /etc/hosts <(ssh somehost cat /etc/hosts)
                //multiline
                    cat <<EOF
                    input
                    on multiple lines
                    EOF
        //redirect variables
            grep hello <<< $cmdResult
    
    //use < > to redirect streams to each other
        //can use numbers to redirect streams other than stdout (1)
            //EG
                //redirects stdout and stderr of cmd to filename
                    cmd &>filename
                //redirects stdout of cmd to stderr		
                    cmd >&2	
        //redirect any stream manlly (including the over 6 streams)
            [streamNum]>&[otherStreamNum]
            //EG
        //redirect stderr to a third stream
            2>&3 

# filesystem links
    //hard links
        //additional name/path for existing file (link contains same content as the original file)
        //any number, within same filesystem/partition
            ln [fileName] [hardLinkName]
    //symbolic/soft
        //link just points to anouther file
            ln -s [fileName] [softLinkName]
        //useful to symlink binaries to your ~/.local/bin 
