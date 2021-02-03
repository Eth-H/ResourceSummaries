sudo mkfs.ext4 /dev/sdb
sudo mkfs.vfat /dev/sdb1
sudo dd status=progress if=name-of.iso of=/dev/sdb
