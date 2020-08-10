# setup
//main default options
export FZF_DEFAULT_COMMAND='fd --type f'
export FZF_DEFAULT_OPTS="--layout=reverse --inline-info"
//default completeion
    //trigger
        export FZF_COMPLETION_TRIGGER='~'
    //options
        export FZF_COMPLETION_OPTS='+c -x'
//bash keybindings
    Set FZF_CTRL_T_COMMAND
    Set FZF_CTRL_T_OPTS
    Set FZF_CTRL_R_OPTS
    Set FZF_ALT_C_COMMAND to override the default command
    Set FZF_ALT_C_OPTS to pass additional options

# use

## auto complete
    cd **<TAB>
    vim **<TAB>
    kill -9 <TAB>
    ssh **<TAB>
    unset **<TAB>
    export **<TAB>
    unalias **<TAB>
## bash keybinding
    CTRL-T - Paste the selected files/dirs onto the cli
    CTRL-R - Paste the selected cmd from history onto the cli
    ALT-C - cd into the selected directory

## open tmux pane with fzf
    cat /usr/share/dict/words | fzf-tmux -l 20% --multi --reverse
