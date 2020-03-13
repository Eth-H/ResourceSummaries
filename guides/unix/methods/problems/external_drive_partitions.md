# external drive is readonly
likely caused by lack of permission

## sol 1
    //change permissions of drive 
    chown -R [user]:[user] /mnt/mountedDriveDir


## sol 2
    //if you automount partions in fstab, change initial permissions
    vim /etc/fstab
        UUID=...    0 0
