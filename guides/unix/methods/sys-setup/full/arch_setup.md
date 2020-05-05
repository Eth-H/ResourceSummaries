# links 
    https://wiki.archlinux.org/index.php/Installation_Guide
    https://wiki.archlinux.org/index.php/Linux_console/Keyboard_configuration
    https://wiki.archlinux.org/index.php/Wireless_network_configuration
    https://wiki.archlinux.org/index.php/Network_configuration

    https://www.youtube.com/watch?v=-fGfZQfeklE

# pre-arch setup
## chosen drive 
    //if partitions already exist
    //can create them from within anouther distrobution
    /
        /dev/nvme0n1p7
    /swap        
        /dev/nvme0n1p8
    /efi 
        /dev/nvme0n1p1   
## check iso
    gpg --keyserver-options auto-key-retrieve --verify archlinux-version-x86_64.iso.sig
    pacman-key -v archlinux-version-x86_64.iso.sig
## burn iso 
    dd if=[isoPath] of=/dev/[usbDrive] status="progress" bs="40"

# after booted into iso
## temp setup iso
    //keymaps 
        //temp
            localectl list-keymaps | grep uk 
            loadkeys uk
    //check in uefi mode
        ls /sys/firmware/efi/efivars

    //network connection
        //network 
            //if not done on boot, get interface and setup
                iwconfig
                ip link set [interface] up
            //search 
                //scan for wifi
                    iwlist [interface] scan | less
            //or 
                wifi-menu
                
        //uni
            sudo mount /dev/nvme0n1p10 /mnt
            cp /mnt/storage/Iu/SecureW2_JoinNow.run ~
        //check conenction
            ip link
            ping archlinux.org

    //ensure sys clock accurate 
        timedatectl set-ntp true

## partition
    //get info 
        fdisk -l /dev/sdx 
        //The disk's partition table 
            Disklabel type: gpt if GPT
            Disklabel type: dos if MBR.
        //get file type of efi
             minfo -i /dev/sdxY :: | grep 'disk type'
    //create partitions 
        //do in gparted on anouther disk
        //local fdisk commands
    
    //format partition (with file system)
        mkfs.ext4 /dev/sdX1
        //swap
            mkswap /dev/sdX2
            swapon /dev/sdX2
    //mount filesystems
        sudo mount /dev/[rootPartition] /mnt  
## select mirrors 
    /etc/pacman.d/mirrorlist
## install essential packages
    pacstrap /mnt base base-devel linux linux-firmware man-db man-pages
dhcpcd netctl vim s-nail intel-ucode

## configure system
    //gen fstab file
        genfstab -U /mnt >> /mnt/etc/fstab
    //chroot into system
        arch-chroot /mnt
    //timezone
        ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
        hwclock --systohc
    //localization
        vim /etc/locale.gen
            //uncomment relevant lang files 
        locale-gen
        vim /etc/locale.conf
            LANG=en_US.UTF-8
        vim /etc/vconsole.conf
            KEYMAP=uk
    //network
        vim /etc/hostname
            myhostname
        vim /etc/hosts
            127.0.0.1	localhost
            ::1		localhost
            127.0.1.1	myhostname.localdomain	myhostname
        pacman -S networkmanager
        systemctl enable networkmanager
    //recreate Initramfs (normally uneccesary) 
        mkinitcpio -P
    passwd
    //setup boot manager
        //need mounted efi 
        pacman -S grub efiboomgr
        pacman -S os-prober ntfs-3g
	mkdir /boot/efi
	mount /dev/nvme0n1p1 /boot/efi
        grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUBbootloader
        grub-mkconfig -o /boot/grub/grub.cfg
    //finish    
        exit
        unmount -R /mnt 
        reboot
    
# active setup
    //users
        useradd -m -g wheel emera
        passwd emera
        vim /etc/sudoers
            add user        
            %wheel ALL=(ALL) ALL
   //graphics 
        pacman -S xorg-server xorg-xinit
        pacman -S xfce4
        pacman -S xfce4-terminal 
        vim ~/.xinitrc
            exec xfce4-session
        pacman -S lightdm lightdm-gtk-greeter
        systemctl enable lightdm.service
        //intel driver that may be requried
            pacman -S xf86-video-intel    
    //network (if required)
        nmtui
