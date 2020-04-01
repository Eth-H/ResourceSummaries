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
    mkdir /mnt/debinst
    mount /dev/hda1 /mnt/debinst
    mkdir /mnt/debinst/home
    mount /dev/hda3 /mnt/debinst/home

## get debootstrap
### manual
    mkdir /mnt/debinst/work
    cd /mnt/debinst/work
    wget http://ftp.debian.org/debian/pool/main/d/debootstrap/debootstrap-udeb_0.3.3_i386.udeb
    ar -x debootstrap-udeb_0.3.3_i386.udeb
    tar zxvpf data.tar.gz
    export DEBOOTSTRAP_DIR=`pwd`/usr/lib/debootstrap
    export PATH=$PATH:`pwd`/usr/sbin
### apt 
    apt install binutils debootstrap

## create base system (run debootstrap)
    debootstrap --arch [amd64 | i386] [FLAVOR] /mnt/debinst http://ftp.debian.org
## 

## config system (mostly from chroot)
    //gen fstab file
        genfstab -U /mnt >> /mnt/etc/fstab
    //initialise chroot
        mount -t proc proc /mnt/debinst/proc
        mount -o bind /dev /mnt/debinst/dev
        //mount --bind /dev/pts /mnt/debinst/dev/pts
        LC_ALL= chroot /mnt/debinst /bin/bash
    //timezone
    //localization
    //users

### network
    echo Hostname > /etc/hostname 
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
    echo -e "127.0.0.1tlocalhost.localdomaintHostname" > /etc/hosts

### install kernel
    //ready built
      apt-cache search linux-image
      apt-get install linux-image-2.6-686-smp
    //install custom deb kernel
      dpkg -i kernel.deb
      sudo apt install kernel.deb -y

### install needed packages
    sudo apt install gvim vifm git ...

### clean up
    exit
    umount /mnt/debinst/{dev,proc,home} /mnt/debinst;
    swapoff
