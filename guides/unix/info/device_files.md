/dev device files/nodes allow you to interact with a devices device driver
with old kernels devices assigned device files in the order the kernel finds them

permissions
    ls -l /dev
    brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
    Permissions, Owner, Group, Major Device Number, Minor Device Number, Timestamp, Device Name

    first bit per line is the device type
        c - character
            transfer data one char at a time
            lots of pseudo devices (aren't actually connected to the machine)
                /dev/null /dev/urandom
        b - block
            transfer data in fixed-sized blks (data blks)
            hardrive, filesystem
        p - pipe
            allow >=2 processes to communicate (like c but to processes (not devices))
        s - socket
            facilitate comms between processes, can communicate to many processes at once
    device nums
        major: repersents device driver used
        minor: tells kernel which unique device it is in the driver class (EG 0 = device 1)

common device names
    SCSI Devices
        small computer system interface 
        protocol allows comms between disks, printers, otehr peripherals
        /dev/sda - First hard disk, /dev/sdb - Second hard disk, /dev/sda3 - Third partition on the first hard disk
    Pseudo Devices
        /dev/zero - accepts and discards all input, produces a continuous stream of NULL (zero value) bytes on read
        /dev/null - accepts and discards all input, provides EOF when read
        /dev/random - provides variable-length stream of numbers on read
        /dev/full - generates a disk full err on write, provides null characters on read
    PATA Devices
        older HD protocol
            /dev/hda - First hard disk, /dev/hdd2 - Second partition on 4th hard disk
sysfs
    virtual filesystem mounted to /sys
    vs /dev: /dev interact with device, /sys view info and manage device, doesnt contain device nodes

udev
    //old way of creating nodes
        mknod /dev/sdb1 b 8 3
    //process
        now udev automatically creates/rms device files if they connected or not
        udevd daemon gets msgs about devices from kernel ->
        udevd parse info and match data with rules from /etc/udev/rules.d ->
        create device nodes and symbolic links for those devices 
    //view udev db and sysfs with udevadm
        udevadm info --query=all --name=/dev/sda
list device info
    //blk devices
        lsblk
    //USB Devices
        lsusb 
    //PCI Devices
        lspci 
    //SCSI Devices
        lsscsi 

dd 
    reads input from a file or data stream and writes it to a file or data stream.
    //if, of: read from/output to file (not stdin/stdout)
    //bs: blk size, read/write this many bytes per time (can use k m abbreviations)
    //count: num blks to cp
    dd if=/home/pete/backup.img of=/dev/sdb bs=1024 
    dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
