sudo apt install plymouth-themes
sudo update-alternatives --install /usr/share/plymouth/themes/default.plymouth 
default.plymouth /usr/share/plymouth/themes/"path/to-your-plymouth.plymouth" 100


// if using latest kernel
sudo update initramfs -u
//chose specific kernel
sudo update initramfs -c -k [kernel-ver]
ls -al /var/lib/initramfs-tools/
