# install pkgs
## xfce4
    //battery plugin: batttery indicator for panel, may need to add manully
    //whiskermenu: better looking more modern menu
    sudo apt install xfce4 xfce4-terminal xfce4-battery-plugin xfce4-whiskermenu-plugin
# theme
    cp [.../themeName] /usr/share/themes/themeName
    cp [.../xfce4] ~/.config/xfce4

# ways to start xorg server with correct de/wm
xinit (startx frontend)
    put start cmd in x conf file
        ~/.xinitrc
        ~/.xprofile
    EG
        echo "exec xfce4-session" > ~/.xsession
display manager (lightdm, gdm)
    put start cmd in x conf file
        //any xinit file
        ~/.xsession
    if not using any x conf file
        add de.desktop file to /usr/share/xsessions/ubuntu.desktop
        //set that desktop file to auto
            sudo vim /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
            #sudo sed -i "/user-session/ s/[currentDefaultDesktop]/[newDefaultDesktop]/" /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
