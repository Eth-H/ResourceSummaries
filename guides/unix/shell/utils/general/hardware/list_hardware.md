# proc files
    cat /proc/cpuinfo
    cat /proc/meminfo 
    cat /proc/version
    cat /proc/scsi/scsi
    cat /proc/partitions

# ls cmds
//cpu
    lscpu
//pci buses and connected devices
    lspci
//usb buses and connected devices
    lsusb
//scsi devices
    lsscsi
//all hardware
    sudo lshw -short
//block devices (HDD partitions, opticla drives, flash drives)
    lsblk

# dmidecode, read from dmi tables/SMBOIS data structures 
## access via alias
    //processor, memory, bios
    sudo dmidecode -t {}
## access by handle
https://en.wikipedia.org/wiki/System_Management_BIOS#Structure_types
man dmidecode
    sudo dmidecode -t [handleNum]


# not preinstalled
// all hardware, good loking summary 
    inxi -Fxxxz
// all hardware
    hwinfo --short
