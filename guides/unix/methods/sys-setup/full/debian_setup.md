https://debian-handbook.info/browse/stable/sect.installation-steps.html#sidebar.bootloader-dual-boot
https://wiki.ubuntu.com/DebootstrapChroot
https://www.debian.org/releases/lenny/ia64/apds03.html.en
https://wiki.debian.org/Debootstrap
https://www.debian.ohttps://www.debian.org/relhttps://www.debian.org/releases/buster/amd64/index.en.htmleases/buster/amd64/index.en.htmlrg/releases/buster/amd64/index.en.html
https://www.linuxquestions.org/questions/debian-26/how-to-install-debian-using-debootstrap-4175465295/
https://www.linux.com/news/cli-magic-installing-debian-gnulinux-using-debootstrap/

# install without iso mtds
    hardisk install
        install from chroot
        install from existing linux

# hardisk install
requires debian/ubuntu base system
if using live system setup network and locale manually

## partition disk
    mkswap /dev/hda2
    swapon /dev/hda2
    mke2fs -j -b 4096 -O dir_index /dev/hda1
    mke2fs -j -b 4096 -O dir_index /dev/hda3
    mkdir /mnt/deb
    mount /dev/hda1 /mnt/deb
    mkdir /mnt/deb/home
    mount /dev/hda3 /mnt/deb/home

## get debootstrap
### manual
    mkdir /mnt/deb/work
    cd /mnt/deb/work
    wget http://ftp.debian.org/debian/pool/main/d/debootstrap/debootstrap-udeb_0.3.3_i386.udeb
    ar -x debootstrap-udeb_0.3.3_i386.udeb
    tar zxvpf data.tar.gz
    export DEBOOTSTRAP_DIR=`pwd`/usr/lib/debootstrap
    export PATH=$PATH:`pwd`/usr/sbin
### apt 
    apt install binutils debootstrap

## create base system (run debootstrap)
    sudo debootstrap 
    --arch=[amd64 | i386] \
    --variant=minbase \
    [FLAVOR] \
    [BUILD_DIR] \
    http://ftp.uk.debian.org/debian

    sudo debootstrap \
    --arch=amd64 \
    bullseye \
    . \
    http://ftp.uk.debian.org/debian

    //if systemd err
        sudo chown root:root [BUILD_DIR]
        sudo chmod 755 [BUILD_DIR]

## config system (mostly from chroot)
### gen fstab file
    //manual
        //get uuid of mounted parition
            sudo blkid | grep -w UUID=
        cp /etc/fstab /mnt/etc/fstab
        vi /mnt/etc/fstab
            //replace root uuid with uuid of mounted partition
    //if arch install scripts
        genfstab -U /mnt > /mnt/etc/fstab
        
### initialise chroot
    //manual
        mount -t proc proc /mnt/deb/proc
        mount -o bind /dev /mnt/deb/dev
        mount -o bind /sys /mnt/deb/sys
        //if neccessary, but may have to restart to umount
            sudo mount -t proc /proc proc/
            sudo mount --rbind /sys sys/
            sudo mount --rbind /dev dev/
            //mount --bind /dev/pts /mnt/deb/dev/pts
        LC_ALL=C 
        chroot /mnt/deb /bin/bash
    //if arch install scripts
        arch-chroot
### timezone
    ln -sf /usr/share/zoneinfo/Region/City /etc/localtime

### setup locale
if not using a server need to config and generate locales
    dpkg-reconfigure locales
    //or directly
        vi /etc/locale.gen 
        //uncomment your locale, EG
            de_DE.UTF-8 UTF-8
            de_DE ISO-8859-1
            de_DE@euro ISO-8859-15
        locale-gen
        vi /etc/locale.conf 
            LANG=de_DE.UTF-8
#### keyboard
    dpkg-reconfigure keyboard-configuration
    //or directly
        vi /etc/default/keyboard
        XKBMODEL="pc105" #keyboard model
        XKBLAYOUT="uk" #keyboard layout
        XKBVARIANT=""
        XKBOPTIONS="grp:alt_shift_toggle"
        BACKSPACE="guess"
        //change model and country layout, get options from
            /usr/share/X11/xkb/rules/base.lst

### network
    echo -e `hostname` >> /etc/hostname
    //echo -e "127.0.0.1\tlocalhost\n127.0.1.1\t`hostname`" >> /etc/hosts
    echo -e \ "127.0.0.1\tlocalhost\n::1\tlocalhost\n127.0.1.1\t`hostname`.localdomain `hostname`" >> /etc/hosts


    //need to setup interfaces manually if not using network-manager
    vim /etc/network/interfaces
        ## The loopback network interface
        auto lo
        iface lo inet loopback

        ## The primary network interface (eth0)
        #auto eth0

        # DHCP
        #iface eth0 inet dhcp

        # Static IP
        #iface eth0 inet static
        #	address 192.168.0.1
        #	netmask 255.255.255.0
        # 	broadcast 192.168.0.255
        #	gateway 192.168.0.254
#### no DHCP
    echo -e "search domainnamennameserver 192.168.0.253nnameserver 192.168.0.254" > /etc/resolv.conf

### users
    passwd
    useradd username
    usermod -aG sudo username

### install and config bootloader
    sudo apt install grub os-prober
    //check if efi or mbr
        ls /sys/firmware/efi
    //efi
        //make sure your efi partition is mounted
        sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=debian-grub
        //tool to manage efi partition
            sudo apt install efibootmgr
    //mbr
        sudo grub-install --target=i386-pc /dev/sdX
    sudo grub-mkconfig -o /boot/grub/grub.cfg

### install kernel
    //ready built
      apt-cache search linux-image
      apt-get install linux-image-amd64
      //apt-get install linux-image-2.6-686-smp
    //install custom deb kernel
      dpkg -i kernel.deb
      sudo apt install kernel.deb -y

### install needed packages
    //if minimal image
        sudo apt install build-essential systemd iproute2 ca-certificates
        sudo apt install man-db wget curl linux-kernel-headers-[version]
    sudo apt install gvim vifm git ...

### clean up
    exit
    umount /mnt/deb/{dev,proc,home} /mnt/deb; //if not rebooting
    // unmount -R /mnt 

    swapoff
    reboot
