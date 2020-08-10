# systemd-nspawn

> much more powerfull chroot
> separate namespace container
> fits containerising a full system rather than just an app

- install
    sudo apt install systemd-container

//Creates isolated containers, has separate mount point, process tree
    debootstrap --arch=amd64 unstable my_deb/
    //Get in container, --network-bridge=br0: Add network set
        systemd-nspawn -D my_deb {}
    //Boot into container, remember change root pw in passwd, 
        systemd-nspawn -bD my_deb

//machinectl
//Control state of systemd based VM
    //-a: status of all running containers
        machinectl {} 
    //status: status of specific container, login: login, switchoff: poweroff, -s kill: kill forcefully, -M: View logs
    machinectl {} {[containerName]}

