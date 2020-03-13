# links
    https://forum.manjaro.org/t/kernel-panic-not-syncing-vfs-unable
    https://forum.manjaro.org/t/kernel-panic-not-syncing-vfs-unable-to-mount-root-fs-on/21226
    https://forum.manjaro.org/t/restore-manjaro-boot/3350
    https://forum.manjaro.org/t/grub-boot-not-working-with-efi/44329
    https://forum.manjaro.org/t/creating-a-new-os-independent-grub-2-bootloader/3150/2
    https://forum.manjaro.org/t/unable-to-set-manjaro-grub-as-default/50611/4

# commands to get infomation
## efi
	efibootmgr -v
## all partitions
	sudo parted -l
	sudo blkid
## mounted systems
	findmnt -s
	findmnt /boot/efi

# boot problems 
## problem 1
after linux grub-updates or you install a new system, the arch boot loader can get replaced, we aim to fix this
  debian/ubuntu grub cannot boot arch linux, but arch linux grub can boot both
### sol 1
aim to make sure arch grub is always used
#### option 1
    add custom entry to all other OS bootloaders to multiboot to or configfile from manjaro grub.cfg
        nano /boot/grub/custom.cfg
            #!/bin/sh
            exec tail -n +3 $0
            # This file provides an easy way to add custom menu entries.  Simply type the
            # menu entries you want to add after this comment.  Be careful not to change
            # the 'exec tail' line above.
            menuentry 'Manjaro GNOME    menu' {
            insmod part_gpt 
            insmod fat
            search --no-floppy --fs-uuid --set=root CF2E-B0AD
            chainloader /EFI/manjaro/grubx64.efi 
            }
				
#### option 2 
     set all other OS’s grub to its own partition so that whenever there’s an update in the other OS’s it won’t 
     become default system grub (make majaro grub default first). But remember to update-grub in Manjaro to incorporate new update in other OS new kernel
    //log into manjaro from debian grub
        //press c in grub menu
        grub> search.file /boot/intel-ucode.img root
        grub> configfile /boot/grub/grub.cfg
        run commands
            sudo grub-install /dev/sda --force
            sudo update-grub

        //EG sda7 = Ubuntu, sda10 = Kubuntu
        boot into ubuntu and run
        sudo grub-install --force /dev/sda7
        
        boot into kubuntu and run
        sudo grub-install --force /dev/sda10

### sol 2
setup debian grub so that it can boot arch
  vim /boot/grub/custom.cfg
    menuentry "Manjaro - multiboot " {
      insmod part_gpt
      insmod ext2
      search --no-floppy  --fs-uuid --set=root [manjaro root partition UUID]
      chainloader /boot/grub/x86_64-efi/core.efi
    }

    menuentry "Manjaro - chainload " {
        insmod part_gpt
      insmod fat
      search --no-floppy  --fs-uuid --set=root [esp_partition UUID]
      chainloader /EFI/Manjaro/grubx64.efi
    }

    menuentry "Manjaro - configfile "  {
      insmod part_gpt
      insmod ext2
      search --no-floppy  --fs-uuid --set=root [manjaro root partition UUID]
      configfile /boot/grub/grub.cfg
    }

    menuentry "Manjaro - vmlinuz " {
      insmod part_gpt
      insmod ext2
      search --no-floppy  --fs-uuid --set=root [manjaro root partition UUID]
      linux	/boot/vmlinuz-4.19-x86_64 root=UUID=[manjaro root partition UUID] rw
      initrd	/boot/intel-ucode.img /boot/initramfs-4.19-x86_64.img
    }				
