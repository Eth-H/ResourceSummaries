linux os abstraction lvs
    hardware: cpu, mem, disk, network ports, ...
    physical layer: machine computation (0s and 1s)
    kernel layer: talk to hardware
        process and memory management, device communication, system calls, sets up our filesystem
    user space: shell, programs, graphics, ...

privilege levels 
    kernel mode
        hardware, network
    user mode
        small amount mem space and cpu access
    lvs correspond to protection rings
        different rings of privilege control
        Ring #0: kernel, ring#3: user mode apps

sys calls
    provide user space kernel a way to ask for kernel to do something
    sys calls api has a fixed num services with a unique id

    programs (EG ls) sys call wrapper invokes sys call -> exes a trap -> caught by sys call handler -> ref sys call in sys call table -> exe func -> return to user mode with return status

    view sys calls made by cmd
        strace ls

manage installation
    can have multiple kernels for grub to boot
    install general/recommended or specific version, then any other pkgs such as linux-headers, linux-image-generic

    get activate kernel
        uname -r
    update all pkgs (including kernel)
        sudo apt dist-upgrade

kernel location
    /boot/
        vmlinux //kernel
        initrd //tmp fs used before loading kernel
        System.map //symbolic lookup table
        config //kernel config, need to compile to edit loaded modules
    can get rid of  unused kernels
kernel modules
    code that can be on demand loaded into kernel (even when booted generally)
    
    //currently loaded
        lsmod
    //load module (and dependancies) from /lib/modules/(kernel version)/kernel/drivers 
        sudo modprobe bluetooth
    sudo modprobe -r bluetooth
    //add config file to load/stop loading modules during boot
        /etc/modprobe.d/peanutbutter.conf
            options peanut_butter type=almond 
            blacklist peanut_butter


