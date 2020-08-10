# tmux

> terminal multipluxer

## shell

- list all bound keys

tmux list-keys

- list every tmux

tmux list-commands

- list every session/window/pane/pid

tmux info

- reload config

tmux source-file ~/.tmux.conf

- list sessions

tmux ls

[prefix] s

- attach to session and detact other clients connected to it

tmux attach -d -t {session id}

- detach session
    - current

    tmux detach 

tmux detach -t {session id}

[prefix] d

:attach -d

- kill sessions

    - specific
    
    tmux kill-session -t {mysession}
    tmux kill-ses -t {mysession}
    
    - all
    
    tmux kill-session -a

    - all but one

    tmux kill-session -a -t {mysession}

- new session

    tmux new-session -s <name>

    :new -s {mysession}

## default keybindings
- prefix

Ctrl + B

### sessions

- rename session

    [prefix] $

- move session
    - previous
    
        [prefix] (
    
    - next

        [prefix] )
                
### windows
- create window

    [prefix] c

- rename current window

    [prefix] ,
- Close current window

    [prefix] &
- move window
    - via previous/next/number

        [prefix] p

        [prefix] n

        [prefix] [0 to 9]
- Reorder window, swap window number 2(src) and 1(dst)

    swap-window -s 2 -t 1
- Move current window to the left by one position

    swap-window -t -1
### panes
- toggle last active pane

    [prefix] ;
- split pane vertically/horizontally

    [prefix] %

    [prefix] "
- move the current pane left/right

    [prefix] {

    [prefix] }
- switch to pane to the direction

    [prefix] up/right/down/left
- toggle synchronize-panes(send command to all panes)

    :setw synchronize-panes
- toggle between pane layouts

    [prefix] Spacebar
- switch to next pane

    [prefix] o
- show pane numbers

    [prefix] q
- switch/select pane by number

    [prefix] q 0 ... 9
- toggle pane zoom

    [prefix] z
- convert pane into a window

    [prefix] !
- resize current pane height(holding second key is optional)

    [prefix] + Up
    [prefix] Ctrl + Up 
    [prefix] + Down
    [prefix] Ctrl + Down 
- resize current pane width(holding second key is optional)

    [prefix] + Right
    [prefix] Ctrl + Right 
    [prefix] + Left
    [prefix] Ctrl + Left 
- close current pane

    [prefix] x

### copy mode
- use vi keys in buffer
    :setw -g mode-keys vi
- enter copy mode

    [prefix] [

- enter copy mode and scroll one page up

    [prefix] PgUp
- quit mode

    q
- go to top/bottom line

    g, G
- scroll up, scroll down

    up, down
- move cursor left, down, up, right

    h, j, k, l

- move cursor forward one word at a time, move cursor backward one word at a time

    w, b

- search forward/backward

    /, ?
    
- next/previous keyword occurance

    n, N
- start/clear/copy selection

    Spacebar, Esc, Enter
- paste contents of buffer_0

    [prefix] ]
- display buffer_0 contents

    :show-buffer
- copy entire visible contents of pane to a buffer

    :capture-pane
- Show all buffers

    :list-buffers
- Show all buffers and paste selected

    :choose-buffer
- Save buffer contents to buf.txt
j
    :save-buffer buf.txt
- delete buffer_1

    delete-buffer -b 1
    
### misc
- enter command mode

    [prefix] :
- set OPTION for all sessions/windows

    :set -g OPTION

    :setw -g OPTION

### help
- show every session, window, pane, etc...

    tmux info
- show shortcuts

    [prefix] ?			
