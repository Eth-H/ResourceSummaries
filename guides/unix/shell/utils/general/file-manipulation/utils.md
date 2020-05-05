# perl tools
## rename/(search/replace within) multiple files
        repren
            # full rename of filenames, directories, and contents foo -> bar:
            repren --full --preserve-case --from foo --to bar .
            # recover backup files whatever.bak -> whatever:
            repren --renames --from '(.*)\.bak' --to '\1' *.bak
        rename 
            #inconsistent behavious across distros, not recommended
            # same as above, using rename, if available:
            rename 's/\.bak$//' *.bak
    #to replace all occurrences of a string in place, in one or more files:
        perl -pi.bak -e 's/old-string/new-string/g' my-files-*.txt

# monitor file processing
    pv, pycp, pmonitor, progress, rsync --progress, dd status=progress (block-level)


