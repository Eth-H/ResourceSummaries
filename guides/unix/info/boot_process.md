BIOS (Basic Input/Output System) 
    initializes the hardware and uses Power-on self test (POST) to check hardware readyness (sys integrity), load bootloader
    boot HD -> find boot block -> look to mbr or gpt (to find how to boot sys)
    mbr
        first HD sector first 512 bytes
        code to lauch anouther program that will load the bootloader
UEFI
    modern BIOS alternative (Unified extensible firmware interface)
    GPT format intended for use with EFI, though first sector of a GPT disk is reserved for a protective MBR for BIOS booting
    stores all the startup info in an .efi file
    .efi and bootloader stored on a special EFI system partition
    

Bootloader
    loads kernel into mem and then starts it with a set of kernel params
    grub: universal linux standard
        use e to edit boot params
            initrd - specifies location of initial RAM disk
            BOOT_IMAGE - where the kernel image is located
            root - location of the root filesystem, kernel searches inside this location to find init. represented by it's UUID or the device name (/dev/sda1)
            ro - mounts the fileystem as read-only mode
            quiet - don't see background display messages during boot
            splash - lets the splash screen be shown
        naming conventions
            (hd0) First hard disk /dev/sda (or /dev/hda)
            (hd1) Second hard disk /dev/sdb (or /dev/hdb)
            (hd0,0) First hard disk, first partition /dev/sda1 (or /dev/hda1)
            (hd1,0) Second hard drive, first partition /dev/sdb1 (or /dev/hdb1)
            (hd1,1) Second hard drive, second partition /dev/sdb2 (or /dev/hdb2)

kernel
    when loaded, immediately initializes devices and mem, main job is to load up the init process
    initrd (initial ram disk): file containing tmp root fs containing essential modulues/drivers kernelneeds to manage initial hardware setup/boot. Then initrd file replaced with actual root fs
    initramfs
        modern initrd alternative
        tmp root fs built into kernel
    after initramfs root mounted read-only for fsck integrity check, then remounts in read-write mode


init
    first process that gets started, starts and stops essential service process on the sys
