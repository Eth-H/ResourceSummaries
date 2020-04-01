# change greeter
    sudo apt install slick-greeter
    sudo vim /etc/lightdm/lightdm.conf
        greeter-session=slick-greeter

# change theme
    update-alternatives --config desktop-background
    # /etc/lightdm/lightdm-gtk-greeter.conf
