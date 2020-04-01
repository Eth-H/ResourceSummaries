#to xfce4
    //battery plugin: batttery indicator for panel, may need to add manully
    //whiskermenu: better looking more modern menu

    sudo apt install xfce4 xfce4-terminal xfce4-battery-plugin xfce4-whiskermenu-plugin
    echo "xfce4-session" > ~/.xsession
    cp [path to your xfce4 config folder] ~/.config/xfce4

# changing default environment
## universal and recommended
    //add desktop/window manager startup cmd to ~/.xsession
        vim ~/.xsession
            exec xfce4-session
## ubuntu only
    //get sessions
    ls /usr/share/xsessions
    //change default session, manually or auto
        sudo vim /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
        sudo sed -i "/user-session/ s/[currentDefaultDesktop]/[newDefaultDesktop]/" /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
