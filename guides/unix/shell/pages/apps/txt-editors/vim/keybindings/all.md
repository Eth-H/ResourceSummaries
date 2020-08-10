# nani
    % - move to matching character (default supported pairs: '()', '{}', '[]' - use <code>:h matchpairs</code> in vim for more info)
# Change mode
    from normal mode to
        command mode- : 
        insert- any insert command (EG i)
        visual manual/line/block- v, V, ctrl + v
        selection- gh
        operator pending- any command that leaves an operation pending (eg y, d)			
        replace, virtual replace - R,gR
    back to normal- esc, Ctrl + [

# normal mode
## motions (cursor movement)
can prefix any motion with a count

    h,j,k,l - mv left/down/up/right
    H,M,L - mv top/middle/bottom of screen
    w,e - jump forwards to the start/end of a word
    W,E - start/end but counts puncuation as part of the word
    b - jump backwards to the start of a word
    B - backwards to start but counts puncuation as part of the word
    0,$ - jump to the start/end of the line
### go
    g_,^ - jump to the last/first non-blank char of the line
    gg,G - go to the first/last line of the document
    [num]gg, [num]G - go to specifc line number 
### to key
    fx,tx - jump to next/beforenext occurrence of chars x
    Fx,Tx - jump to previous/afterprevious occurence of chars x
    ;,, - repeat previous f, t, F or T movement in direction/backwards
### bracket jumps
    },{ - jump to next/prev paragraph (func/block)
    ),( - jump to next/prev sentance
    ],[ - jump to next/prev section, if not defined by vimscript/plugin will default to { or }
### mv cursor
    zz - center cursor on screen
    <C-y>,<C-e> - move screen up/down one line (without moving cursor)
    <C-b>,<C-f> - move back/forward one full screen
    <C-d>,<C-u> - move/back forward 1/2 a screen
## operators
can prefix any operator with a count

generally can suffix with a motion

can suffix a visual selection to act on it

some operators put you in operator pending mode until anouther operator or motion is typed
### copy/cut/paste (uses the unamed (local vim) clipboard)
    y - yank, operator pending mode
    yy,y_ - yank (copy) a line
        2yy - yank (copy) 2 lines
        yw - yank (copy) the characters of the word from the cursor position to the start of the next word
    p - put (paste) the clipboard after cursor
    P - put (paste) before cursor
    d - delete, operator pending mode
    dd - delete (cut) a line
        2dd - delete (cut) 2 lines
        dw - delete (cut) the chars of the word from the cursor position to the start of the next word
    D - delete (cut) to the end of the line
    x - delete (cut) character
    //use global clipboard
        //vim compiled with +clipboard
        "+y
        "+p

### Editing
    r - replace a single character
    J - join line below to the current one with one space in between
    u,<C-r> - undo/redo
    . - repeat last command
    //see c in insert mode section
    >>,<< - indent text right/left

#### special
    gJ - join line below to the current one without space in between
    gwip - reflow paragraph

## text obj cmds
vim only, require +textobjects at compile time

can be used in visual or operator pending modes

### select a non-block obj
start with a: select a obj including whitespace

start with i: select inner obj which doesnt include whitespace

    aw - a word
    iw - inner word
    aW - a WORD
    iW - inner WORD
    as - a sentance
    is - inner sentance
    ap - a paragraph
    ip - inner paragraph
### select between block/delms

a variations: include the delm

i variations: exclude the delm

    a],a[  - a [] block
        EG a[xxxxxxxxx]czc da] -> aczc
    i],i[  - inner [] block
    a),a(,ab - a () block
    i),i(,ib - inner () block
    a>,a<, a <> block
    i>,i<, inner <> block
    a},a{,aB - a {} block
    i},i{,iB - inner {} block
    a",a',a` - a quotes block
    i",i',i` - inner quotes block
    at - tag block
        select contents between 2 matching tags
        if on the same line but before any tag starts, select the outermost tag
    it - tag block
## registers

registers are stored in ~/.viminfo, and will be loaded again next restart

    "[register letter/symbol][operator] - operate on register
    :reg - show registers content
    "xy - yank into register x
    "xp - paste contents of register x
    <C-r>[register l/s] - access registers in insert mode
### types
    " - unnamed/default
        ""p = p
    + - global/system
    numbered registers
        0 - contains latest yank
        1-10 - contains latest del, 1 = most recent
    read only registers
        . - last inserted (i mode) text 
        % - current file path relative dir vim opened in
        : - last executed cmd, good with :@
        # - alternate file, last edited file
        <C-^> - switch between current and alternate
    = - last search
    macros - macros are stored in a custom register
        EG add a semi colon to your w macro
            :let @W='i;' 

# visual mode
mark text

    v,V,<C-v> - start visual mode in normal/line/block
    V - start linewise visual mode
    Ctrl + v - start visual block mode
    o - move to other end of marked area
    O - move to other corner of block
    aw - mark a word
    ab, aB - a block with ()/{}
    ib,iB - inner block with ()/{}
    Esc - exit visual mode

## Visual commands
    > - shift text right, < - shift text left, 2<, 2>
    y,x,d - yank/del/del highlighting text
    d - delete marked text
    ~ - switch case	
    u - all lower case, U - all upper case
    //recomended to be manually remapped
    Ctrl + c - copy text to global clipboard
    r - replace            
## normal and visual mode
### macros
    qa - record macro a
    q - stop recording macro
    @a - run macro a
    @@ - rerun last run macro
			
# Insert mode - inserting/appending text
- go to insert mode
```
    i, I - insert: before the cursor, beginning of the line
    a, A - insert (append): after the cursor, at end of line
    o, O - append (open) a new line: below the current line, above the current line
    c - change, operator pending
    cc - change (replace) entire line
    C - change (replace) to the end of the line
    c$ - change (replace) to the end of the line
    ciw - change (replace) entire word
    cw - change (replace) to the end of the word
    s, - delete {} and substitute text: character, line (same as cc)
```
# Command mode (ex/vi cmd mode)
    :help keyword - open help for keyword
    :close - close current pane
    :! [commandName]... - execute cmds in shell
    # - refer to current file name
    ! tee: redirect output of vim commands
    :source,:so - source vimscript from a file
    :@ - run a register as if it where a vi cmd
    vimscript keybindings
        <C-y> - ctrl y
        <S-y> - shift y
## ranges
    prefix cmds
    1,7 - line 1 to 7
    and/or use a cmd symbol that selects
        % - entire file
        +,- - offset from current line
        'm - marks
## format util cmds (most from ed/ex)
all can be used as a standalone cmd with a range or combined with anouther

    :...d - del
    :...p - print
    :...g - globally apply subsequent cmd to all lines matching supplied regex
    :...v - above but lines that dont match
    EG 
        :.,+21g/foo/d
        :.,$v/bar/d
        :.,+25p
        :% g/foo/s/bar/zzz/g - for every line containing foo substitute all bar with zzz
    :...! - bang, apply external cmds
        Eg :1,$!sort

### replace
    :s/old/new/g - replace all old with new throughout current line
    :%s/old/new/g - replace all old with new throughout file
    :%s/old/new/gc - replace all old with new throughout file with confirmations
## read
    :r [fileName] - read file into current file at cursor pos
    :r ! [commandName] - read cmd into current file at cursor pos
## edit modifiable file state
    :set ma, :set noma	
## read/check key mappings
    //<TAB> <Space> <C-[x]>  <A-[x]> <S-[x]>
    :map [key], imap, vmap, omap
    :versbose map [key]
## Saving and exiting
    :saveas file - save file as
    :w - write (save) current file/buffer
    :wa - save all
    :w !sudo tee % - write out the current file using sudo
    :wq,:x,ZZ - write and quit
    :q - quit (fails if there are unsaved changes)
    :q!,ZQ - quit and throw away unsaved changes
    :wqa - write and quit on all tabs

## Marks
    :marks - list of marks
    ma - set current position for mark A
    `a - jump to position of mark A
    y`a - yank text to position of mark A

## search
    /pattern - search for pattern, ?pattern - search backward for pattern
        //EG /\<wordToFind\>
    \vpattern - 'very magic' pattern: non-alphanumeric characters are interpreted as special regex symbols (no escaping needed)
    n, N - repeat search in same/opposite direction
    :noh - remove highlighting of search matches
### Search in multiple files
    :vimgrep /pattern/ {file} - search for pattern in multiple files
        e.g.:vimgrep /foo/ **/*
    :cn - jump to the next match
    :cp - jump to the previous match
    :copen - open a window containing the list of matches

## Working with multiple files
### move window
    <C-w> ws - split window
    <C-w> ww - switch windows
    <C-w> wq - quit a window
    <C-w> wv - split window vertically
    <C-w> wh - move cursor to the left window (vertical split)
    <C-w> wl - move cursor to the right window (vertical split)
    <C-w> wj - move cursor to the window below (horizontal split)
    <C-w> wk - move cursor to the window above (horizontal split)
    <C-w> wn - new split with new file
### buffers
can refer to file via its buffer number in command mode #[bufferNumber]

    :e [file] - edit a file in a new buffer
    :sp [file], :vsp [file] - open a file in a new buffer {} split window: horizontally, vertically
    :b [bufferNum] - switch to active buffer
    :bn, bnext - go to the next buffer, :bp, :bprev - go to the previous buffer
    :bd [bufferNum] - delete a buffer (close a file)
    :ls, :buffers - list all open buffers
    :new, :vnew - new split with a new unamed file: horizontally, vertically
### tabs
    :tabnew - open new tab
    :tabnew [file], :tabe [file] - open a file in a new tab
    Ctrl + wT - move the current split window into its own tab
    gt, :tabnext, :tabn - move to the next tab, gT, :tabprev, :tabp - move to the previous tab xgt - move to tab number x
    :tabmove # - move current tab to the #th position (indexed from 0)
    :tabclose, :tabc - close the current tab and all its windows
    :tabonly, :tabo - close all tabs except for the current one
    :tabdo command - run the command on all tabs (e.g. :tabdo q - closes all opened tabs)
### current working dir
    :pwd
- change cwd to dir of currently open file (sets the cwd for all windows in Vim):

    :cd %:p:h
- change cwd to dir only for the current window 

    :lcd %:p:h
                        
## sessions
### specific path
- create

    :mksession ~/mysession.vim
- access from in/outside vim

    :source ~/mysession.vim
    vim -S ~/mysession.vim
### current session
    :mks session1.vim
    vim -S session1.vim
        
## other
- check paths in vims shell

    :echo syntastic#util#system('echo "$PATH"')
- reload .vimrc
    - while editing

        :so %
    - in general

        :so $VIMRC

# plugins
## plugin manager
- vundle

    :PluginInstall - install packages in vimrc
- vim-plug
```
:PlugInstall - Install plugins
:PlugUpdate - Install or update plugins
:PlugClean! - Delete removed plugins
:PlugUpgrade - Upgrade Vim-Plug
:PlugStatus - List plugins and current status
:PlugDiff - Display changes made during updates
:PlugSnapshot[1] [/output/path] - Generate script for restoring current plugins
```

## fugitive (git interface)
    :G - git status
    :fugitive help
## navigation
### file explorer
#### nerd
    ctrl E - open file explorer (need to add this binding yourself)
    ctrl N - basic autocomplete on current selected keyword
    r - reload (use after creating new files)
- open a file
```
o, enter - open in previosu window
t - open in new tab, T - t, open in new tab silently (in the background)
i - open in new split
```
- change CWD

    cd - change CWD to selected dir
    CD - change tree root to CWD
- navigation

    <C-j> - go to next sibling   
    <C-k> - go to prev sibling 
### fuzzy file finder	
#### ctrlpvim (file finder)
    ctrl p - open file finder
    :help ctrlp-mappings - get key bindings
- in file finder

    ctrl-f, ctrl-b - navigate between modes
#### fzf
- file names
    - list files in entered path

        :Files [path]
    - list files via name

        :Locate [patturn]
    - list Buffers

        :Buffers
    - list git files

        :GFiles

    :Filetypes
- search windows
    :Windows
- search maps
    :Maps
- file contents
    - Change active colour scheme
        :Colors
    - search in file, can enter line number or patturn
        - all loaded buffers, curent loaded buffer

            :Lines

            :BLines, :Line

   - search tags
        - all loaded buffers, current loaded buffer 

            :Tags

            :BTags

- item contents
   - : commands

        :Commands

   - file history, command history, search history

       History, History:, History/

   - list commits, list commits for current buffer

       :Commits, :BCommits

- ways to open a selected item

    ctrl-t - tab split 

    ctrl-x - split

    ctrl-v - vsplit

## generic ide features
### linting (syntax checking)
    multi language
        ale
            //help                                   
                :help ale-options 
                :help ale-integration-options                       
                :help ale-[language]-[linter] 
        syntastic (generic syntax checker)
            relies on externel syntax checkers
                :SyntasticInfo - see avaliable checkers				
    single language
        flake8
            <F7> - run flake8 on current python file
### syntax highlighting
    vim-polygot
        
### autocomplete
    YCM (multi-language code complete)
        trigger jedi (python autocomplete)
            ctrl + space
### code folding
    SimpylFold (built in)
        create fold
            zf{motion}  or {Visual}zf //create fold flexibilly
            [zount]zF: create a fold for [count] lines
            :{range}fo[ld]  //create a fold for the lines in {range}
        del folds
            zd - del fold at cursor or in selection
            zD - recursive zd, del nested folds
            zE - del all folds in window
        zc/zC - close a fold at cursor nomally/recusively
        zo/ZO - open a fold at cursor nomally/recusively
        zx - update folds: undo manually opened/closed folds
### lsp
    coc
        some cmds provided out of the box
        cmds and actions provided by lsp plugins (generally vs-code)
        :CocCommand [plugin|area].[cmd|cmdGroup]...[cmd]
            dcoument.renameCurrentWord -> i -> type new var name
        :call CocAcion()
        //extensions, diagnostics, commands, actions, outline
        :CocList {}

        use grep (generally fzf is better)
        :CocSearch term 

## programming utils
### vim commentary
    [num]gcc //comment lines
    gc[movement action]
        gcap
        gc{
    v -> gc
    :7,17Commentary
    :g/TODO/Commentary
### vim surround
    //when surround is operator pending for a delm certain keys have different vals
        t -> tag, b -> bracket
        ( { [ -> ( { [, ) } ] -> } ) ] with space
            EG "txt" cs"} -> { txt }; "txt" cs"{ -> {txt}
    //replace delms
        cs[del][replaceDelm]
        //can refer to tag delms as t
            cst[replaceDelm]
    //delete
        ds[delmToRM]
    //add
        // specifc
            ys[motion][delm]
        // around a word
            ysiw[delm]
        // around line
            yss[delm]
        // visual
            v -> S[delm]

## vim session
    //open vim with certain session
        vim --servername [session]
    //save session, saves to g:session_directory 
        :SaveSession [sessionName]
    :OpenSession
    :RestartVim
    :CloseSession
    :DeleteSession
    //view vim script generated for this session
    :ViewSession
    //only apply command to current tab
        :OpenTabSession, :SaveTabSession, :AppendTabSession, :CloseTabSess

## Ropevim (refractor, code-assits, extra commands)
    contains lots of commands to do different things
    recommended to disable, may use later if more keyboard functionality is required
    because there are so many commands some may need to be remapped (EG <C-Space> )
    see external file for all keymaps and commands
    see https://github.com/python-rope/ropevim/blob/master/doc/ropevim.txt for more info
