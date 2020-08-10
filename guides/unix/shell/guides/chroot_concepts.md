export LFS=/mnt/lfs
cd $LFS

mount -t proc proc $LFS/proc
mount -o bind /dev $LFS/dev
mount -o bind /sys $LFS/sys
sudo mount -t proc /proc $LFS/proc/
sudo mount --rbind /sys $LFS/sys/
sudo mount --rbind /dev $LFS/dev/

umount -v $LFS/dev/pts
umount -v $LFS/dev
umount -v $LFS/proc
umount -v $LFS/sys
umount -v $LFS/run
umount $LFS

umount --recursive $LFS
