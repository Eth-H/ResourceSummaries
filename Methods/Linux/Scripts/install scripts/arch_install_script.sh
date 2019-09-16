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
