need non-free firmware for a device to work, generally network card or gpu
if you didnt get the firmware in the installation process, you may need to fetch it

# deb
## mtd 1
    add non-free sources
    /etc/apt/sources.list
        deb http://deb.debian.org/debian stretch main contrib non-free
        deb-src http://deb.debian.org/debian stretch main contrib non-free
        deb http://deb.debian.org/debian-security/ stretch/updates main contrib non-free
        deb-src http://deb.debian.org/debian-security/ stretch/updates main contrib non-free
        deb http://deb.debian.org/debian stretch-updates main contrib non-free
        deb-src http://deb.debian.org/debian stretch-updates main contrib non-free
    apt update 
    //all
        // default free, firmware-linux-free
        apt install firmware-linux-nonfree
    //specific
        apt install firmware-iwlwifi
    sudo modprobe iwlwifi

## mtd 2
    grab firmware form
        http://cdimage.debian.org/cdimage/unofficial/non-free/firmware/
    extract and put in /lib/firmware
