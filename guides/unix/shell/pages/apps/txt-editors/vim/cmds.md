## open multiple files
- in buffers

    vim [file1] [file2]...
- in horizontal splits

    vim -o [file1] [file2]...
- in vertical splits

    vim -O [file1] [file2]...

## open in mode
- a binary file
    vim -b key.asc
- read only mode
    vim -R file
    view file
- retro vi mode
    vim -C file


## other
- file differences
    vim -d file1 file2
    vimdiff file1 file2
- dont use a swap file
    vim -n
- list swap files
    vim -r
