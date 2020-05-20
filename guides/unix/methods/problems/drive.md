# permissions
## external drive is readonly
likely caused by lack of permission

### sol 1
    //change permissions of drive 
    chown -R [user]:[user] /mnt/mountedDriveDir


### sol 2
    //if you automount partions in fstab, change initial permissions
    vim /etc/fstab
        UUID=...    0 0

# ntfs
## cant see drive
    sudo apt-get install ntfs-3g
## wont mount
    Mounting volume... $MFTMirr does not match $MFT (record 0)
### sol1
    ntfsfix -b /dev/sdb1
### sol2
    wont fix weird stuff windows has done to the disk
    will fix some ntfs disk problems
    //from windows dos
    chkdsk /f [driveLetter]:
