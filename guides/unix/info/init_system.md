start/stop essentional processes

# system V
    traditional, themes and cmds generally work with any other init sys
    starts and stops processes sequentially
        slow, strict startup proccesses (need certain order), task blocking
    runlevel modes
        0: Shutdown
        1: Single User Mode
        2: Multiuser mode without networking
        3: Multiuser mode with networking
        4: Unused
        5: Multiuser mode with networking and GUI
        6: Reboot
    executes scripts in current runlevels config
        /etc/rc.d/rc[runlevel number].d
        /etc/init.d
    change default runlevel
        /etc/inittab
        //via grub
            //from grub
                press e in for boot params, add rl num to end of linux kernel cmd
            //from desktop
                /etc/default/grub
                    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash [rl num]"    
    change rl (to 0 or 6 will shutdown/reboot)
        init [rl]
    get current rl
        who -r

## service cmds 
    //List services
        service --status-all
    //Start a service
        sudo service networking start
    //Stop a service
        sudo service networking stop
    //Restart a service
        sudo service networking restart

# upstart
    event and job model
    /usr/share/upstart
    list jobs and their config
        /etc/init
        EG
        /etc/init/networking.conf
            start on runlevel [235]
            stop on runlevel [0]
            sets up networking on runlv 2, 3 or 5
            stop networking on runlv 0
    process
        load job/configs -> startup event triggers jobs for upstart to run -> these jobs startup new events and their jobs -> go until all jobs started

## job cmds
    //list jobs
        initctl list
    //view job
        initctl status networking
    //start/stop/restart manually
        sudo initctl start networking
        sudo initctl stop networking
        sudo initctl restart networking
    //Manually emit an event
        sudo initctl emit some_event

# systemd
/usr/lib/systemd
    configs
        /etc/systemd/system
        /usr/lib/systemd/system

    boot targets
        very similar to rl, each have dependancies to achieve
        main targets
            poweroff.target - shutdown system
            rescue.target - single user mode
            multi-user.target - multiuser with networking
            graphical.target - multiuser with networking and GUI
            reboot.target - restart
            default.target - default, normally graphical.target
        //all targets stored in (and unit files)
            /lib/systemd/system/* 
        /etc/systemd/system/*

        //change active target
            systemctl isolate multi-user.target //= init 3
        //change default runlevel
            systemctl enable multi-user.target
            systemctl set-default multi-user.target

    process
        load configs -> determines boot goal/target -> figure boot target dependancies and activate them

    units (*.service)
        each service has a unit file
        systemd is flexible and robust so it can do lots of stuff, so has different unit types
        soon as unit activated, everything below it gets activated
        types
            Service units: services we've been starting and stopping, unit files end in .service
            Mount units: mount filesystems, unit files end in .mount
            Target units: group together other units, the unit files end in .target
    EG unit service file
        [Unit]
        Description=My Foobar
        Before=bar.target

        [Service]
        ExecStart=/usr/bin/foobar

        [Install]
        WantedBy=multi-user.target
## cmds
//List units
    systemctl
    systemctl list-units
//View status of unit
    systemctl status networking.service
//Start, stop, restart a service
    sudo systemctl start networking.service
    sudo systemctl stop networking.service
    sudo systemctl restart networking.service
//Enable, disable a unit
    sudo systemctl enable networking.service
    sudo systemctl disable networking.service

# control power states (turn off)
    //shutdown now, in 2 secs with msg to users
        sudo shutdown -h now
        sudo shutdown -h +2 "server is going down now"
    //restart
        sudo shutdown -r now
        sudo reboot
    //or use reboot cmd: shutdown, reboot, intant sys reset (no shutdown occurs)
        reboot -p
        reboot
        reboot -f
    //R E I S U B key strokes
        ALT + PrintScreen (SysRq)  + {} 
            R: //unRaw (take control of keyboard back from X)
            E: tErminate (send SIGTERM to all processes (terminate gracefully))
            I: kIll (send SIGKILL to all processes (force terminate immediately))
            S: Sync (flush data to disk)
            U: Unmount (remount all filesystems read-only)
            B: reBoot //reboot -f
        //enabled if non-zero
            cat /proc/sys/kernel/sysrq

# logging in
    login through new tty 
        getty
            opens a tty port -> runs /bin/login for a login prompt
            rerun by swapping tty (CTRL+ALT+F[1-7])
            starts at rl 1 to 6
        desktop login
            gdm/xdm/kdm/lightdm display manager
            starts at rl 5, or 2 if have rc.d script in /etc/init/[dmName]
    login through ssh at rl 2 to 3
        OenSSH (sshd) server
