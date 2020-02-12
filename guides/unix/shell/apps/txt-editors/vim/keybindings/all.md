# Change mode
    from normal mode to
        command mode- : 
        insert- any insert command (EG i)
        visual- v, V, ctrl + v
        selection- gh
        operator pending- any command that leaves an operation pending (eg y, d)			
    back to normal- esc, Ctrl + [
# normal mode
    Editing
        r - replace a single character
        J - join line below to the current one with one space in between
        gJ - join line below to the current one without space in between
        gwip - reflow paragraph
        xp - transpose two letters (delete and paste)
        u - undo
        Ctrl + r - redo
        . - repeat last command
    Cursor movement
        h - move cursor left, j - move cursor down, k - move cursor up, l - move cursor right
        H - move to top of screen, M - move to middle of screen, L - move to bottom of screen

        w - jump forwards to the start of a word, W - jump forwards to the start of a word (words can contain punctuation)
        e - jump forwards to the end of a word, E - jump forwards to the end of a word (words can contain punctuation)
        b - jump backwards to the start of a word, B - jump backwards to the start of a word (words can contain punctuation)

        % - move to matching character (default supported pairs: '()', '{}', '[]' - use <code>:h matchpairs</code> in vim for more info)
        0 - jump to the start of the line, $ - jump to the end of the line
        g_ - jump to the last non-blank character of the line, ^ - jump to the first non-blank character of the line
        gg - go to the first line of the document, G - go to the last line of the document
        5G - go to line 5
        fx - jump to next occurrence of character x, tx - jump to before next occurrence of character x
        Fx - jump to previous occurence of character x, Tx - jump to after previous occurence of character x
        ; - repeat previous f, t, F or T movement, , - repeat previous f, t, F or T movement, backwards
        } - jump to next paragraph (or function/block, when editing code), { - jump to previous paragraph (or function/block, when editing code)
        zz - center cursor on screen
        Ctrl + e - move screen down one line (without moving cursor)
        Ctrl + y - move screen up one line (without moving cursor)
        Ctrl + b - move back one full screen
        Ctrl + f - move forward one full screen
        Ctrl + d - move forward 1/2 a screen
        Ctrl + u - move back 1/2 a screen
        Tip Prefix a cursor movement command with a number to repeat it. For example, 4j moves down 4 lines.
    Cut and paste (uses the unamed (local vim) clipboard)
        yy - yank (copy) a line
        2yy - yank (copy) 2 lines
        yw - yank (copy) the characters of the word from the cursor position to the start of the next word
        y$ - yank (copy) to end of line
        p - put (paste) the clipboard after cursor
        P - put (paste) before cursor
        dd - delete (cut) a line
        2dd - delete (cut) 2 lines
        dw - delete (cut) the characters of the word from the cursor position to the start of the next word
        D - delete (cut) to the end of the line
        d$ - delete (cut) to the end of the line
        x - delete (cut) character
        
        specify clipboard (make sure have up-to vim installed for global clipboard compatibility)
            use global clipbaord
                "+y
                "+p
# visual mode
mark text
    v - start visual mode, mark lines, then do a command (like y-yank)
    V - start linewise visual mode
    o - move to other end of marked area
    Ctrl + v - start visual block mode
    O - move to other corner of block
    aw - mark a word
    ab - a block with ()
    aB - a block with {}
    ib - inner block with ()
    iB - inner block with {}
    Esc - exit visual mode
## Visual commands
    > - shift text right, < - shift text left, 2<, 2>, //or use . to repeat > or <
    y - yank (copy) marked text
    d - delete marked text
    ~ - switch case	
    u - all lower case, U - all upper case
    //recomended to be manually remapped
    Ctrl + c - copy text to global clipboard
    r - replace            
## normal and visual mode
    Macros
        qa - record macro a
        q - stop recording macro
        @a - run macro a
        @@ - rerun last run macro
			
# Insert mode - inserting/appending text
    go to insert mode
        i, I - insert: before the cursor, beginning of the line
        a, A - insert (append): after the cursor, at end of line
        o, O - append (open) a new line: below the current line, above the current line
        ea - insert (append) at the end of the word
        cc - change (replace) entire line
        C - change (replace) to the end of the line
        c$ - change (replace) to the end of the line
        ciw - change (replace) entire word
        cw - change (replace) to the end of the word
        s, - delete {} and substitute text: character, line (same as cc)
## access registers
    //global clipboard
        CTRL-R *
    //unamed clipboard
        CTRL-R "
		
# Command mode	
    :help keyword - open help for keyword
    :close - close current pane
    :! [commandName]... - execute cmds in shell
    # - refer to current file name
    ! tee: redirect output of vim commands

## insert into command file
    :r [fileName]
    :r ! [commandName]
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
    :wq or :x or ZZ - write (save) and quit
    :q - quit (fails if there are unsaved changes)
    :q! or ZQ - quit and throw away unsaved changes
    :wqa - write (save) and quit on all tabs
## Registers
    :reg - show registers content
    "xy - yank into register x
    "xp - paste contents of register x
    Tip Registers are being stored in ~/.viminfo, and will be loaded again on next restart of vim.
    Tip Register 0 contains always the value of the last yank command.
## Marks
    :marks - list of marks
    ma - set current position for mark A
    `a - jump to position of mark A
    y`a - yank text to position of mark A

## Search and replace
    /pattern - search for pattern, ?pattern - search backward for pattern
        //EG /\<wordToFind\>
    \vpattern - 'very magic' pattern: non-alphanumeric characters are interpreted as special regex symbols (no escaping needed)
    n - repeat search in same direction, N - repeat search in opposite direction
    :s/old/new/g - replace all old with new throughout current line
    :%s/old/new/g - replace all old with new throughout file
    :%s/old/new/gc - replace all old with new throughout file with confirmations
    :noh - remove highlighting of search matches
    Search in multiple files
        :vimgrep /pattern/ {file} - search for pattern in multiple files
        e.g.:vimgrep /foo/ **/*
        :cn - jump to the next match
        :cp - jump to the previous match
        :copen - open a window containing the list of matches
## Working with multiple files
### move window
    Ctrl + ws - split window
    Ctrl + ww - switch windows
    Ctrl + wq - quit a window
    Ctrl + wv - split window vertically
    Ctrl + wh - move cursor to the left window (vertical split)
    Ctrl + wl - move cursor to the right window (vertical split)
    Ctrl + wj - move cursor to the window below (horizontal split)
    Ctrl + wk - move cursor to the window above (horizontal split)
    Ctrl + wn - new split with new file
### buffers
    //refer to file via its buffer number in command mode #[bufferNumber]
    :e [file] - edit a file in a new buffer
    :b [bufferNum] - switch to active buffer
    :bn, bnext - go to the next buffer, :bp, :bprev - go to the previous buffer
    :bd [bufferNumber] - delete a buffer (close a file)
    :ls, :buffers - list all open buffers
    :sp [file], :vsp [file] - open a file in a new buffer {} split window: horizontally, vertically
    :new, :vnew - new split with a new unamed file: horizontally, vertically
### Tabs
    :tabnew - open new tab
    :tabnew [file], :tabe [file] - open a file in a new tab
    Ctrl + wT - move the current split window into its own tab
    gt, :tabnext, :tabn - move to the next tab, gT, :tabprev, :tabp - move to the previous tab
    xgt - move to tab number x
    :tabmove # - move current tab to the #th position (indexed from 0)
    :tabclose, :tabc - close the current tab and all its windows
    :tabonly, :tabo - close all tabs except for the current one
    :tabdo command - run the command on all tabs (e.g. :tabdo q - closes all opened tabs)
### current working dir
    :pwd
    //change cwd to dir of currently open file (sets the cwd for all windows in Vim):
    :cd %:p:h
    //change cwd to dir only for the current window 
    :lcd %:p:h
                        
## Sessions
    //specific path
        //create
            :mksession ~/mysession.vim
        //access from in/outside vim
            :source ~/mysession.vim
            vim -S ~/mysession.vim
    //current session
        :mks session1.vim
        vim -S session1.vim
        
## other
    check paths in vims shell
        :echo syntastic#util#system('echo "$PATH"')
    reload .vimrc
        //while editing
            :so %
        //in general
            :so $VIMRC

# plugins
## plugin manager
    vundle  
        :PluginInstall - install packages in vimrc
    vim-plug
        :PlugInstall - Install plugins
        :PlugUpdate - Install or update plugins
        :PlugClean! - Delete removed plugins
        :PlugUpgrade - Upgrade Vim-Plug
        :PlugStatus - List plugins and current status
        :PlugDiff - Display changes made during updates
        :PlugSnapshot[1] [/output/path] - Generate script for restoring current plugins
## fugitive (git interface)
    :G - git status
    :fugitive help
## navigation
### file explorer
#### nerd
    ctrl E - open file explorer (need to add this binding yourself)
    ctrl N - basic autocomplete on current selected keyword
    open a file
        o, enter - open in previosu window
        t - open in new tab, T - t, open in new tab silently (in the background)
        i - open in new split
    r - reload (use after creating new files)
    change CWD
        cd - change CWD to selected dir
        CD - change tree root to CWD
    navigation
        <C-j> - go to next sibling   
        <C-k> - go to prev sibling 
### fuzzy file finder	
#### ctrlpvim (file finder)
    ctrl p - open file finder
    :help ctrlp-mappings - get key bindings
    //in file finder
        ctrl-f, ctrl-b - navigate between modes
#### fzf
    :[Option]
        //file names
            //list files in entered path
                Files [path]
            //list files via name
                Locate [patturn]
            //list Buffers                    
                Buffers
            //list git files
                GFiles
            Filetypes
       //search windows
            Windows
       //file contents
            //Change active colour scheme
                Colors
            //search in file, can enter line number or patturn
                //all loaded buffers, curent loaded buffer
                    Lines   
                    BLines    
           //search tags
                //all loaded buffers, current loaded buffer 
                    Tags
                    BTags
       //item contents
           //: commands
                Commands
           //history, command history, search history
               History, History:, History/
           //list commits, list commits for current buffer
               Commits, BCommits                           
    //ways to open a selected item
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
    SimpylFold
        zc - close a fold
        zo - open a fold

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
