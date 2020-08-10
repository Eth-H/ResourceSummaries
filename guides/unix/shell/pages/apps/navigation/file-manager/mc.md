# mc
## shell
- get installation paths
    
    mc -F
    
- make your own skins
```
mkdir ~/.local/share/mc/skins 
cp /usr/share/mc/skins/default.ini ~/.local/share/mc/skins/
sed -i -E 's/^(.* = (gray|brightred|brightgreen|yellow|brightblue|brightmagenta|brightcyan|white);.*)$/\0;bold/' ~/.local/share/mc/skins/default.ini
vim /home/emera/.config/mc/ini
    //line 85 is skin-default
    //line 122 is hidden files
```
## keys
- Switch column: tab
- Bottem repersents: F1 – F10 
- move mc to background: ctrl+o
- select multiple files: insert on each file
- change default editor: select file -> F2 -> 1 -> select-editor
- change file permissions: F9 -> File -> chown -> select category -> r, w, x
- toggle hidden files: Alt + .

- simulate F keys

    F10: Esc + 0

    F1-10: Esc + 1-10
