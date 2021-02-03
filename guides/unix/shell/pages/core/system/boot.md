# boot
> manage booting into the system

## efibootmgr
- list all efi images
    efibootmgr

- verbose info
    efibootmgr -v

- change boot order
    efibootmgr -o 2,1,4,3,5,0,...

- add entry in UEFI boot menu, (run by grub)
    efibootmgr -c -d /dev/sda -p 7 -L <label> -l \EFI\<label>\grubx64.efi

- rm boot entry 
    sudo efibootmgr -b <bootnum> -B

- set boot entry active or inactive, \*=active
    sudo efibootmgr -b <bootnum> -a
    sudo efibootmgr -b <bootnum> -A
