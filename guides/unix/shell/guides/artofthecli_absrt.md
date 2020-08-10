# bash
    files
        on login
            ~/.bash_profile or .profile
        on new shell
            ~/.bashrc
    aliases
        alias ll="ls -latr"
    debugging
        set -x 
        set -v (logs raw inp)
        set -e abort on errs
        set -u to detect unset variable usages
        set -o pipefail,    to abort on errors within pipes
        trap use on exit or err

        set -euo pipefail
        trap "echo 'error: Script failed: see failed command above'" ERR
    subshells
        (cd /some/other/dir && other-command)
    variable expansion
        ${name:?error message}
        input_file=${1:?usage: $0 input_file} #bash script with single arg
        output_file=${2:-logfile} #additional optional params, will choose default
        i=$(( (i + 1) % 5 )) #arithmatic expansion
        {1..10} #sequences
        ${var%suffix} ${var#prefix} #trim strings
            EG
                var=foo.pdf -> echo ${var%.pdf}.txt -> foo.txt
        mv foo.{txt,pdf} some-dir
        cp somefile{,.bak} # -> cp somefile somefile.bak
        mkdir -p test-{a,b,c}/subtest-{1,2,3}
        #expansion order
            brace expansion; tilde expansion, parameter and variable expansion, arithmetic expansion, and command substitution (done in a left-to-right fashion); word splitting; and filename expansion
            {1..20} -> {$a..$b} #illegal, instead use
                seq $a $b
                for((i=a; i<=b; i++)); do ... ; done
        # treate output of cmd as a file 
            diff /etc/hosts <(ssh somehost cat /etc/hosts)
        cat <<EOF
        input
        on multiple lines
        EOF

    bash jobs
    keybindings //to format/learn
        ctrl-r: to search through command history (after pressing, type to search, press ctrl-r repeatedly to cycle through more matches
        //flexible move/del
            ctrl-w: to delete the last word
            ctrl-u: cut from cursor to line start
            ctrl-k: cut from cursor to line end
            ctrl + y: paste from the special clipboard (ctrl + u and ctrl + k save to)

             alt-b, alt-f: to move by word
             ctrl-a/ctrl-e: to move cursor to beginning/end of line

         ctrl-l: to clear the screen
        alt-. : cycles previous args
        alt-* expands a glob
        alt-#: add a # at the beginning and enter it as a comment (or ctrl-a, #, enter), you can then return to it later via command history
         man readline for all the default keybindings in Bash 
        //or, vi keybindings
            set -o vi
        export EDITOR=vim
            ctrl-x ctrl-e will open the current command in an editor for multi-line editing. Or in vi style, escape-v.


    filenames with whitespace
        "$FOO"
        locate -0 pattern | xargs -0 ls -al
        find / -print0 -type d | xargs -0 ls -al
        IFS=$'\n'  prepare to iterate filenames with white space

    find docs
    redirection
    glob expansion //tofinish
        Learn about file glob expansion with * (and perhaps ? and [...]) and quoting and the difference between double " and single ' quotes

    history 
        !cmdNum
        !! last cmd
        !$ last arg
    cd 
        ~ -


    max cmd line arg length
        128k
        grep ARG_MAX /usr/include/linux/limits.h
            #define ARG_MAX 131072 
        find ./ -name '*' -print0 | xargs -0 -n 10 rm #bypass

    sudo
        -u [specifc user] 
        -i [user] //run shell as the users login shell (with their .profile/.login, ...)
            //EG sudo -i sh -c

# external tools 
    screen multiplexers
        screen
        tmux, byobu
        dtach
    interactive value selection
        percol, fzf, fpp
  
# essentional tools
    ssh //todo
        ssh-agent, ssh-add
        port tunnel with -L -D -R
        ~/.ssh/config
            TCPKeepAlive=yes
            ServerAliveInterval=15
            ServerAliveCountMax=6
            Compression=yes
            ControlMaster auto
            ControlPath /tmp/%r@%h:%p
            ControlPersist yes
            #StrictHostKeyChecking=no  #per subnet
            #ForwardAgent=yes  #host or in trusted networks
    mosh #udp alternative

    files
        ls less head tail chown chmod du df mount fdisk mkfs lsblk, inodes

    open sockets or files
        lsof fuser
    uptime
        uptime
        w

    network
       ip or ifconfig, dig, traceroute, route 
        [`mtr`](http://www.bitwizard.nl/mtr/) #better traceroute

        listening
            netstat -lntp or ss -plat (for TCP; add -u for UDP) or lsof -iTCP -sTCP:LISTEN -P -n (which also works on macOS).
    git
    processes
        pstree pgrep pkill
    grep, egrep //tomaster
        -i, -o, -v, -A, -B, and -C
        regexs
    package manager

    kill
        kill -[signalNum] pid
        man [signalNum] signal

    xargs
        Note you can control how many items execute per line (-L) as well as parallelism (-P). If you're not sure if it'll do the right thing, use xargs echo first. Also, -I{} is handy. Examples:

          find . -name '*.py' | xargs grep some_function
          cat hosts | xargs -I{} ssh root@{} hostname

    octal file permissions
        stat -c '%A %a %n' /etc/timezone

    python server
        python -m SimpleHTTPServer 7777 #py2 
        python -m http.server 7777 #py3



# processing files and data
    search files
        sed awk 
        ag #silver searcher
        rg #ripgrep
    sort stuff
        sort 
            -n -h
            sort -k1,1 | sort -s -k2,2 #sort first by field 2, then by field 1
            -t
                ctrl-v [Tab] or write $'\t' #tab literal
        uniq
            -u -d 
        comm
        cut, paste, join  #manipulate text files
    wc #count newlines (-l), characters (-m), words (-w), bytes (-c)
    tee #copy from stdin to a file and stdout
    datamash #advanced grouping

    convert / deal with  file types
        To convert HTML to text: lynx -dump -stdin
        pandoc README.md --from markdown --to docx -o temp.docx #many formats

        xmlstarlet #handle xml
        jq  #handle JSON
        jid and jiq #handle JSON, interactive use
        shyaml # handle YAML

        csvkit: in2csv, csvcut, csvjoin, csvgrep # handle Excel, CSV

        s3cmd #convenient 
        s4cmd #faster, Amazon S3
        #binary files
            hd, hexdump, xxd #hex dumps 
            bvi, hexedit, biew #binary editing
            strings #extract strings
            xdelta3 #binary diffs
        iconv, uconv #convert text/unicode encodings
            # Displays hex codes or actual names of characters (useful for debugging):
            uconv -f utf-8 -t utf-8 -x '::Any-Hex;' < input.txt
            uconv -f utf-8 -t utf-8 -x '::Any-Name;' < input.txt
            # Lowercase and removes all accents (by expanding and dropping them):
            uconv -f utf-8 -t utf-8 -x '::Any-Lower; ::Any-NFD; [:Nonspacing Mark:] >; ::Any-NFC;' < input.txt > output.txt


    export LC_ALL=C # set locale to C, disabling |18n routines for traditional byte sort order

    #To replace all occurrences of a string in place, in one or more files:
    perl -pi.bak -e 's/old-string/new-string/g' my-files-*.txt

    rename/(search/replace within) multiple files
        repren
            # Full rename of filenames, directories, and contents foo -> bar:
            repren --full --preserve-case --from foo --to bar .
            # Recover backup files whatever.bak -> whatever:
            repren --renames --from '(.*)\.bak' --to '\1' *.bak
        rename 
            #inconsistent behavious across distros, not recommended
            # Same as above, using rename, if available:
            rename 's/\.bak$//' *.bak

    mkdir empty && rsync -r --delete empty/ some-dir && rmdir some-dir
    
    monitor file processing
        pv, pycp, pmonitor, progress, rsync --progress, dd status=progress (block-level)

    Use shuf to shuffle or select random lines from a file.

    patch source code
        diff, patch
        diffstat # diff summary
        sdiff #side by side diff
        vimdiff #compare and edit files
        diff -r tree1 tree2 | diffstat


    split #split files into pieces by size
    csplit #split files into pieces by pattern

    date
        date -u +"%Y-%m-%dT%H:%M:%SZ" #ISO 8601 format
        dateutils: dateadd, datediff, strptime
    zless, zmore, zcat, zgrep #operate on compressed files.
    set file attributes and a lower-level alternative to file permissions
        chattr
        sudo chattr +i /critical/directory/or/file #eg protect against accidental file del

        getfacl, setfacl #save and restore file permissions
            getfacl -R /some/path > permissions.txt
            setfacl --restore=permissions.txt

        create empty files quickly
            truncate #sparse files
            fallocate #ext4, xfs, btrfs and ocfs2 filesystems 
            xfsprogs: xfs_mkfile #almost any filesystems
            mkfile #Solaris, Mac OS

# system debugging
    web
        curl, curl -I, wget, httpie
        //find which socket/process is using bandwidth
            [`iftop`](http://www.ex-parrot.com/~pdw/iftop/)
            [`nethogs`](https://github.com/raboof/nethogs)
        //web servers
            apache: ab
            siege
        //advanced
            [`wireshark`](https://wireshark.org/)
            [`tshark`](https://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html)
            [`ngrep`](http://ngrep.sourceforge.net/)
    htop, iostat, iotop -mxz 15, intel_gpu_top, nvtop
    summary
        dstat, glances
    mem
        free
        vmstat #cached val=linux kernel file cahce mem
    java
        kill -r pid #stacktrace
        JDK: jps, jstat, jstack, jmap
        [SJK tools](https://github.com/aragozin/jvm-tools) #more advanced
    full disk
        [`ncdu`](https://dev.yorhel.nl/ncdu) #saves time over du -sh

    strace, ltrace #helpful if a program is failing/hanging/crashing
        profiling option: -c  
        attach to a running process: -p
        trace child option: -f #avoid missing important calls

    ldd #to check shared libraries
        [never run it on untrusted files](http://www.catonmat.net/blog/ldd-arbitrary-code-execution/)
    gdb #connect to a running process and get its stack traces

    /proc #debugging live problems. 
        /proc/cpuinfo, /proc/meminfo, /proc/cmdline, /proc/xxx/cwd, /proc/xxx/exe, /proc/xxx/fd/, /proc/xxx/smaps (where `xxx` = pid)

    #debugging why something went wrong in the past
        [sar](http://sebastien.godard.pagesperso-orange.fr/) #shows historic statistics on CPU, memory, network, ...

    #deeper systems and performance analyses, 
        stap, ([SystemTap](https://sourceware.org/systemtap/wiki))
        [`perf`](https://en.wikipedia.org/wiki/Perf_%28Linux%29)
        [`sysdig`](https://github.com/draios/sysdig)
    uname -a #general Unix/kernel info
    lsb_release -a #Linux distro info
    
    #faulty hardware/drivers
        dmesg #kernel err msgs

    #delete a file and doesn't free up disk space (via du), check whether the file is in use by a process
        lsof | grep deleted | grep "filename-of-my-big-file"

# one liners
    sort a b | uniq > c   # c is a union b
    sort a b | uniq -d > c   # c is a intersect b
    sort a b b | uniq -u > c   # c is set difference a - b

    pretty-print two JSON files, normalizing syntax, then coloring/paginating res
        diff <(jq --sort-keys . < file1.json) <(jq --sort-keys . < file2.json) | colordiff | less -R

    quickly examine the contents of all files in a directory (EG use /sys and /proc)
        grep . *  #each line is paired with the filename
        head -100 * #each file has a heading

    summing all nums in third column of text file
        awk '{ x += $3 } END { print x }' myfile

    see sizes/dates on a tree of files, better ls -lR
        find . -type f -ls

    have a certain value that appears on some lines, such as an `acct_id` parameter that is present in the URL. tally how many requests for each `acct_id`:
        egrep -o 'acct_id=[0-9]+' access.log | cut -d= -f2 | sort | uniq -c | sort -rn

    to continuously monitor changes
        watch
        EG check changes to files in a directory 
            watch -d -n 2 'ls -rtlh | tail'` 
        EG network settings while troubleshooting your wifi settings with 
            watch -d -n 2 ifconfig
# cmd list
    `expr`: perform arithmetic or boolean operations or evaluate regular expressions
    `m4`: simple macro processor
    `yes`: print a string a lot
    `cal`: nice calendar
    `env`: run a command (useful in scripts)
    `printenv`: print out environment variables (useful in debugging and scripts)
    `look`: find English words (or lines in a file) beginning with a string
    `cut`, `paste` and `join`: data manipulation
    `fmt`: format text paragraphs
    `pr`: format text into pages/columns
    `fold`: wrap lines of text
    `column`: format text fields into aligned, fixed-width columns or tables
    `expand` and `unexpand`: convert between tabs and spaces
    `nl`: add line numbers
    `seq`: print numbers
    `bc`: calculator
    `factor`: factor integers
    [`gpg`](https://gnupg.org/): encrypt and sign files
    `toe`: table of terminfo entries
    `nc`: network debugging and data transfer
    `socat`: socket relay and tcp port forwarder (similar to `netcat`)
    [`slurm`](https://github.com/mattthias/slurm): network traffic visualization
    `dd`: moving data between files or devices
    `file`: identify type of a file
    `tree`: display directories and subdirectories as a nesting tree; like `ls` but recursive
    `stat`: file info
    `time`: execute and time a command
    `timeout`: execute a command for specified amount of time and stop the process when the specified amount of time completes.
    `lockfile`: create semaphore file that can only be removed by `rm -f`
    `logrotate`: rotate, compress and mail logs.
    `watch`: run a command repeatedly, showing results and/or highlighting changes
    [`when-changed`](https://github.com/joh/when-changed): runs any command you specify whenever it sees file changed. See `inotifywait` and `entr` as well.
    `tac`: print files in reverse
    `comm`: compare sorted files line by line
    `strings`: extract text from binary files
    `tr`: character translation or manipulation
    `iconv` or `uconv`: conversion for text encodings
    `split` and `csplit`: splitting files
    `sponge`: read all input before writing it, useful for reading from then writing to the same file, e.g., `grep -v something some-file | sponge some-file`
    `units`: unit conversions and calculations; converts furlongs per fortnight to twips per blink (see also `/usr/share/units/definitions.units`)
    `apg`: generates random passwords
    `xz`: high-ratio file compression
    `ldd`: dynamic library info
    `nm`: symbols from object files
    `ab` or [`wrk`](https://github.com/wg/wrk): benchmarking web servers
    `strace`: system call debugging
    [`mtr`](http://www.bitwizard.nl/mtr/): better traceroute for network debugging
    `cssh`: visual concurrent shell
    `rsync`: sync files and folders over SSH or in local file system
    [`wireshark`](https://wireshark.org/) and [`tshark`](https://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html): packet capture and network debugging
    [`ngrep`](http://ngrep.sourceforge.net/): grep for the network layer
    `host` and `dig`: DNS lookups
    `lsof`: process file descriptor and socket info
    `dstat`: useful system stats
    [`glances`](https://github.com/nicolargo/glances): high level, multi-subsystem overview
    `iostat`: Disk usage stats
    `mpstat`: CPU usage stats
    `vmstat`: Memory usage stats
    `htop`: improved version of top
    `last`: login history
    `w`: who's logged on
    `id`: user/group identity info
    [`sar`](http://sebastien.godard.pagesperso-orange.fr/): historic system stats
    [`iftop`](http://www.ex-parrot.com/~pdw/iftop/) or [`nethogs`](https://github.com/raboof/nethogs): network utilization by socket or process
    `ss`: socket statistics
    `dmesg`: boot and system error messages
    `sysctl`: view and configure Linux kernel parameters at run time
    `hdparm`: SATA/ATA disk manipulation/performance
    `lsblk`: list block devices: a tree view of your disks and disk partitions
    `lshw`, `lscpu`, `lspci`, `lsusb`, `dmidecode`: hardware information, including CPU, BIOS, RAID, graphics, devices, etc.
    `lsmod` and `modinfo`: List and show details of kernel modules.
    `fortune`, `ddate`, and `sl`: um, well, it depends on whether you consider steam locomotives and Zippy quotations "useful"


# macOS
    pkg management: `brew` (Homebrew), `port` (MacPorts)
    clipboard: pbcopy, pbpaste #instead of xclip xsel
    enable the Option key in macOS Terminal as an alt key (**alt-b**, **alt-f**, ...)
        open Preferences -> Profiles -> Keyboard and select "Use Option as Meta key"
    open a file with a desktop app: `open` or `open -a /Applications/Whatever.app`
    spotlight
        search files: `mdfind` 
        list metadata: `mdls`
    macOS based of BSD
        Linux has System V-style Unix and GNU tools
        ps, ls, tail, awk, sed, ... different to linux
        man page has the heading "BSD General Commands Manual." 
        get gnu version
        `gawk` `gsed`
        avoid for cross platform
    macOS release information: `sw_vers`

# windows
    unix shell
        cygwin 
        WSL
        gnu dev tools for windows
            [MinGW](http://www.mingw.org/) and its [MSYS](http://www.mingw.org/wiki/msys)
        [Cash](https://github.com/dthree/cash)
    script Windows system administration tasks
        `wmic`
    networking tools
        `ping`, `ipconfig`, `tracert`, `netstat`
    [many useful Windows tasks](http://www.thewindowsclub.com/rundll32-shortcut-commands-windows)
        `Rundll32`
## cygwin
    cli window: `mintty`
    access the windows clipboard: `/dev/clipboard`
    open an arbitrary file through its registered application: `cygstart` 
    access the windows registry: `regtool`
    cygwin and win paths
    `C:\` -> `/cygdrive/c` on cygwin
    `/` -> `C:\cygwin` on Windows
    cygwin <-> windows-style file paths: `cygpath`
