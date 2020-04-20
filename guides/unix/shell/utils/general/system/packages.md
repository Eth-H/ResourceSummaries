# Package manager 

# debian
## dpkg 
lower lv pkg manager
    // .deb files are packages generated for Debian-based distros, install with dpkg
    // install debian package, cant install dependancies
        sudo dpkg -i /home/user/cowsay.deb
    //remove
        sudo dpkg -r cowsay
    //list packages installed
        dpks -l
    //re-configure package database (fix dpkg corruption problems)
        sudo dpkg --configure -a
## apt
    apt (advanced pkging tool): contains other pkging modulues, can use most other apt cmds
    //apt-get: install/remove/upgrade
        //Update sources (servers with package info/download links) from /etc/apt/sources.list
            sudo apt update
        //Update all/specific installed software
            sudo apt upgrade [packageName]?
        sudo apt dist-upgrade
        //Download/remove software
        //-f: force, rm problomatic package
            sudo apt install [packageName]...
        //rm pkgs without/with their configs
            sudo apt remove [packageName]...
            sudo apt purge [packageName]...
        //get pkg source to certain dir
            sudo apt source [packageName]
        //download but dont install
            sudo apt download [packageName]
        //download pkg change-log and shows installed pkg version
            sudo apt changelog [packageName]
        //check for broken dependancies
            sudo apt-get check
        //search local repos and install build dependancies for pkg
            sudo apt-get build-dep [packageName]
        //Clean/fix
            //Remove half-installed packages
            //rm .deb files from /var/cache/apt/archives
                sudo apt autoclean
            //remove apt cache (rm downloaded .debs from local repo)
                sudo apt clean
            //remove uneccessary software dependancies
                sudo apt autoremove
    //apt-cache: search apt software cache
        //Get info on a package //uses apt-cache
            apt show [packageName]
        //Search for a package //uses apt-cache
            sudo apt search [packageName]
        //get a pkgs dependancies
            apt-cache showpkg [packageName]
        //stats
            apt-cache stats

### aptitude
apt frontend with ncurses and cli tools
    //run ncurses iterface
        aptitude
    //can use any apt cmds with cli
      aptitude ...

#### list explicitly installed programs
      comm -23 <(apt-mark showmanual | sort -u) <(gzip -dc /var/log/installer/initial-status.gz | sed -n 's/^Package: //p' | sort -u)
      comm -23 <(aptitude search '~i !~M' -F '%p' | sed "s/ *$//" | sort -u) <(gzip -dc /var/log/installer/initial-status.gz | sed -n 's/^Package: //p' | sort -u)

      aptitude search '~i !~M' -F '%p' --disable-columns | sort -u > currentlyinstalled.txt
      wget -qO - http://mirror.pnl.gov/releases/precise/ubuntu-12.04.3-desktop-amd64.manifest \
        | cut -f1 | sort -u > defaultinstalled.txt
      comm -23 currentlyinstalled.txt defaultinstalled.txt

# arch
## pacman 
    //-S: sync packages
     //[packageName]: install package, -u: upgrade installed packages, y: download fresh pacakges, --noconfirm: dont ask, --ignore: ignore a packages upgrade
     //s: search for package
      //[packageName]: apply previous option to selected package 				    					    
    //-R [packageName]: remove software
    //-Q: query local packages
     //-u: list outdated packages, -i: view package info, -l: list packages
          //[packageName]: apply previous option to selected package 
    //-U [packageName]: upgrade specific package
            sudo pacman {} {}?...
    //EG Upgrade all packages 
        sudo pacman -Syu

## AUR (arch user repositary)
    //first install base level package group
        pacman -S --needed base-devel
    //manual
        //download package
            git clone https://aur.archlinux.org/package_name.git
        //or go to the AUR website and download snapshot, then extract
            tar -xvf package_name.tar.gz
        //download from link, extract afterwards
            curl -L -O https://aur.archlinux.org/cgit/aur.git/snapshot/package_name.tar.gz
       cd package_name
       //check contents
            less package
        //build with the arch build system
            //--s: resolves and installs dependancies, -i: installs package
                makepkg -si
            //or run makepkg -s and then instal yourself
                pacman -U package_name.pkg.tar.xz
    //aur helpers
            pacman AUR wrappers
        yaourt 
            //install
                
            //can use all pamac commands
                //[package name]: search AUR for package (then type its number), --stats: package installation stats, 
                yaourt {}...
        yay 
            //more modern pacman wrapper
            //pacman syntax

# fedora/RHEL/CentOS
## rpm 
    //Generated for Fedora-based distros
    //-v: verbose, -h: hash marks (% completion)
    //Install
        rpm -i [pkg]
    //Remove
        rpm -e [pkg]
    //Upgrade
        rpm -U [pkg]?
    //List packages
        rpm -q [pkg]
        rpm -qa
## yum 
    //Fedora package manager, automatically updates sources	
    //Upgrade installed software
        //blank: all, --security, [packageName]
            sudo yum update {}?
        //update >=1 pkg to certain version
            sudo yum update-to
        //take obsoletes into acocunt
            sudo yum upgrade
    //Download/remove software
        sudo yum install [pkg]
        sudo yum groupinstall [pkgGroup]
        sudo yum localinstall pkg.rpm
        sudo yum remove [pkg]
        sudo yum downgrade [pkg]
        // remove additional uneeded pkgs
        sudo yum autoremove [pkg]?
        sudo yum reinstall [pkg]
        sudo yum swap [oldPkg] [newPkg]

    //query
        //list avaliable pkgs from repos
            //avaliable, installed, all, kernel
                yum list {}
            //list installed/avaliable pkg groups
                yum grouplist
        yum info [pkg]
        yum groupinfo [pkgGroup] //EG "Web Server"
        //list dependancies
            yum deplist [pkg]
        //pkgs contining queried file
            yum provides [fileFromPkg]
        //search pkg names and desc
            yum search [pkg]
        //info on pkg updates
            yum updateinfo [pkg]
        //desiplay desc and contents of pkg group
            yum grouplist [pkgGroup]
    //repos
        repolist
        repoinfo [enabledYumRepoName]
        //list,install,remove
            repo-pkgs repoName {}
        //download repo data to cache
            makecache
    //troubleshot/maintain
        //check local db for errs
            yum check
        //list: install/update/erase actions
        //info/update/redo: [transactionNum]
            yum history {}
        //delete packages from / clean out pkgs and metadata from - cache
            yum clean packages
            yum clean all


# Building from source 
    //Look for INSTALL txt file
    //cd into direcotry with source code ->  run configure ELF (executable) file to generate system specific makefile ->   run make to compile source code into an ELF ->  
     // run sudo make install to move binary created and required files to system folders (now they can be used anywhere)	
        cd [pathToSourceCode]
        make [sourceCode]
        make install 
        
    git clone [url]
    cd [projectBin]
    mkdir build
    cd build
    cmake ..
    //Raise number after j relative to num cores+1
    make -j8
    sudo make install		
