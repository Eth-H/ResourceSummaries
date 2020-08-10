//chroot, move root somewhere else	
	sudo apt-get update
	sudo apt-get install dchroot debootstrap
	sudo mkdir /test

	sudo vim /etc/schroot/schroot.conf
	//modify
		[saucy]
			description=Ubuntu Saucy
			location=/test
			priority=3
			users=demouser
			groups=sbuild
			root-groups=root
	//Setup with just certain files
		mkdir /chroot
		//add wanted directories -> copy wanted files and needed liabaries
			//Get wanted executables
				mkdir /chroot/{bin}
				cp -v /bin/{bash, ls} /chroot/bin
			//Get needed liabraries	
				mkdir /chroot/{lib, lib64}
				//Check libraries needed to run the wanted executable
					ldd /bin/bash
					ldd /bin/ls
				cp -v /{lib/bib64} /chroot/{lib/lib64}
		//enter chroot
			sudo chroot /chroot/ /bin/bas
		//exit
			exit	
	//Setup with full system 
		//Generate skeleton OS, add --foreign if architectures dont rematch
			debootstrap --arch=amd64 unstable my_deb/
		//Setup process mangagement and add temp home thats lost on exit
			sudo mount -o bind /proc my_deb/proc
			mount -t tmpfs -o size=100m tmpfs /home/user
		//Setup internet
			cp /etc/hosts /chroot/etc/hosts
			sudo cp /etc/resolv.conf /var/chroot/etc/resolv.conf	
		//enter chroot env
			chroot my_deb/ /bin/bash
		//setup graphical applications
			//run outside chroot
				xhost
			export DISPLAY=:0.0
			
		//custom chroot service
			[Unit]
			Description=my_chroot_Service
			[Service]
			RootDirectory=/chroot/foobar
			ExecStartPre=/usr/local/bin/pre.sh
			ExecStart=/bin/my_program
			RootDirectoryStartOnly=yes
			systemctl start my_chroot_Service.service
			
	
//alt setup
    //Generate skeleton OS, add --foreign if architectures dont rematch
        sudo debootstrap --variant=buildd --arch amd64 saucy /test/ http://mirror.cc.columbia.edu/pub/linux/ubuntu/archive/
        sudo chroot /test /debootstrap/debootstrap --second-stage


    sudo vim /etc/fstab
            //edit
                proc /test/proc proc defaults 0 0
                sysfs /test/sys sysfs defaults 0 0	
    //mount within guest
        sudo mount proc /test/proc -t proc
        sudo mount sysfs /test/sys -t sysfs
    //unmount proc filesystems
        sudo umount /test/proc
        sudo umount /test/sys
    //del after use
        rm -rf /test/
