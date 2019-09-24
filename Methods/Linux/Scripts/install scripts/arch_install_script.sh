#yaourt
	#manual AUR method
		sudo pacman -S --needed base-devel git wget yajl
		cd /tmp
		git clone https://aur.archlinux.org/package-query.git
		cd package-query/
		makepkg -si && cd /tmp/
		git clone https://aur.archlinux.org/yaourt.git
		cd yaourt/ && makepkg -si
#screen snipper, uses less dependancies than shutter
pacman -S screenFetch	

#virtualisation
#virtual box
pacman install virtualbox $(pacman -Qsq "^linux" | grep "^linux[0-9]*[-rt]*$" | awk '{print $1"-virtualbox-host-modules"}' ORS=' ')
#add virtual box module to kernel, if further problems https://wiki.manjaro.org/index.php?title=VirtualBox
sudo vboxreload
sudo gpasswd -a $USER vboxusers
#virtualbox guest additions
pamac install virtualbox-guest-utils $(pacman -Qsq "^linux" | grep "^linux[0-9]*[-rt]*$" | awk '{print $1"-virtualbox-guest-modules"}' ORS=' ')#pacman -S virtualbox-guest-dkms
sudo modprobe vboxguest vboxvideo vboxsf
sudo gpasswd -a $USER vboxsf
sudo systemctl enable --now vboxservice.service
#sudo rcvboxdrv
