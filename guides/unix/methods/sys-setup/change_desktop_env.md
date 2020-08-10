# install / theme
## xfce4
    //battery plugin: batttery indicator for panel, may need to add manully
    //whiskermenu: better looking more modern menu
    sudo apt install xfce4 xfce4-terminal xfce4-battery-plugin xfce4-whiskermenu-plugin
# theme
    theme dirs
        local themes - ~/.themes/
        global - /usr/share/themes/
        local keybinding changes, panel settings/items/... - ~/xfce/.config
    sub dirs/files
        gtk icons/styles
            gtk-2.0
            gtk-3.0
        xfce4 theme
            xfwm4
        gtk shortcuts/keybindings (normally bundled with xfwm theme)
            gtk-2.0-key/gtkrc
            gtk-3.0/gtk-keys.css
    icons
        /usr/share/icons
            
    apply 
        cp theme to theme dir
        appearnace window: select gtk theme
        window manager settings: select xfwm theme and its gtk keybingings
        select gtk theme from appearance, and xfce4 theme from window manager settings
    cp [.../themeName] /usr/share/themes/themeName
    cp [.../xfce4] ~/.config/xfce4

# ways to start xorg server with correct de/wm
xinit (startx frontend)
    put start cmd in x conf file
        ~/.xinitrc
        ~/.xprofile
    EG
        echo "exec xfce4-session" > ~/.xinitrc
display manager (lightdm, gdm)
    put start cmd in x conf file
        ~/.xsession
    if not using any x conf file
        add de.desktop file to /usr/share/xsessions/ubuntu.desktop
        //set that desktop file to auto
            sudo vim /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
            #sudo sed -i "/user-session/ s/[currentDefaultDesktop]/[newDefaultDesktop]/" /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
        //or
            /etc/lightdm/lightdm.conf
                user-session=xfce
