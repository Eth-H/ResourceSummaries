# change greeter
    sudo apt install slick-greeter
    sudo vim /etc/lightdm/lightdm.conf
        greeter-session=slick-greeter

# change theme
    update-alternatives --config desktop-background
    # /etc/lightdm/lightdm-gtk-greeter.conf
    # /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
