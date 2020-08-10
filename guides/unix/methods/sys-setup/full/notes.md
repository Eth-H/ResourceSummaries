# setup framework
## totally manual installation (without installer)
### pre-chroot
    setup tmp keymap locale network //if neccessary
    partition
        root 
        swap efi/boot //if dont have already
    write ext4 to partiton
    init swap //if new swap
    makefilesys
    sys bootstrap cmd //pacstrap debootstrap
    genfstab
    mount and chroot
### in chroot
    timezone    
    locales //or set LC_ALL=C
        keyboard
    network
        hostname
        //if no nm
            interfaces
            no dhcp //if neccessary
        install nm and add to init sys
    install bootloader
    setup bootloader
    root pw //if neccessary
    create user(s) acc and pw
    add user(s) to sudoers
    //edit sudoers, add user to a sudo enabled group
    install software //can normally do in the bootstrap step
        install kernel
            if hardware problems, may require a custom/patched kernel
        install bootloader
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
    change wm themes, gtk themes, icons

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
