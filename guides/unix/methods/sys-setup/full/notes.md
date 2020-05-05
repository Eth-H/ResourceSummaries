# setup
## totally manual installation (without installer)
### pre-chroot
    setup tmp keymap locale network //if neccessary
    partition
        root swap
    makefilesys
    sys create cmd //pacstrap debootstrap
    genfstab
### 
    timezone    
    locales //or set LC_ALL=C
    network
        hostname
        //if no nm
            interfaces
            no dhcp //if neccessary
        install nm adn add to init sys
    install bootloader
    setup bootloader
    root pw //if neccessary
    user pw
    edit sudoers, add user to a sudo enabled group
    install custom kernel //if neccessary
    install other essential pkgs //vim git ...
    umount and leave chroot



## customise
    setup graphical install
        install xorg
        install desktop //xfce4
        install wm
            wm
            screensaver
            screenlocker
            power manager
            key agent //seahorse
            terminal emulator
            file manager
            keymap //skhd, if neccessary
            edit ~/.xinitrc //if using startx
            edit ~/.xsession //if using a dm
        install dm and add to init sys //lightdm
        install drivers //intel,nvidia,amd
    change splash/plymouth theme //if a splash screen
    change grub themes
    change de/wm themes //~/.config/xfce4

## install apps
    terminal 
        txt editor
        terminal multiplexer
        tui file manager
    gui
        txt editor
        browser
        virtuallisation software
        screenshooter
    ...
    set app defaults via xdg
