# mocp

> ncurses music player

## config
``` 
mkdir ~.moc
cp usrsharedocmocconfig.example ~.mocconfig
vim ~.mocconfig
```
    gg 222

    Theme = /usr/share/moc/themes/nightly_theme

    XTermTheme = /usr/share/moc/themes/nightly_theme

## keys
- run

`mocp`

- quit
    
    q

### play
- pause

    p, SPACE

- next song

    n

- previous
    
    bb

#### Change play order
- toggle repeat

    R
- toggle suffle

    S
- toggle autonext

    X

### playlist
- move to playlist

    TAB

- add filedirectory
        
    a

- Recuresively add directory 
    
    A
- Del item
    
    d
- clear playlist
    
    C
- Save playlist
    
    V
- switch layout 
    
    l

- edit volumn: -1%, +1%, -5%, +5%,
    
    <, >, (,), .
