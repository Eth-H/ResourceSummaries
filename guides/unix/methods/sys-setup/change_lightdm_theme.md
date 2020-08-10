# change greeter
    sudo apt install slick-greeter
    sudo vim /etc/lightdm/lightdm.conf
        greeter-session=slick-greeter
    //or
        sudo vim /usr/share/lightdm
            //change something
# change theme
    update-alternatives --config desktop-background
    # /etc/lightdm/lightdm-gtk-greeter.conf
    # /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
