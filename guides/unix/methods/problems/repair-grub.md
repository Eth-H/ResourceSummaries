sudo mount /dev/sdXXX /mnt
sudo mount /dev/sdXX /mnt/boot/efi #your sys efi partition
mount -t proc none /mnt/proc
mount -o bind /dev /mnt/dev
mount -t sysfs sys /mnt/sys
chroot /mnt/ /bin/bash

for i in /dev /dev/pts /proc /sys /run; do sudo mount -B $i /mnt$i; done
sudo chroot /mnt
grub-install /dev/sdX
update-grub 
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUBbootloader
grub-mkconfig -o /boot/grub/grub.cfg

