start/stop essentional processes

# system V
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
    default runlevel in
        /etc/inittab
## service cmds (also work in upstart and systemd)
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
    targets to boot into (each have dependancies to achieve)
        poweroff.target - shutdown system
        rescue.target - single user mode
        multi-user.target - multiuser with networking
        graphical.target - multiuser with networking and GUI
        reboot.target - restart
        default.target - default, normally graphical.target
    process
        load configs -> determines boot goal/target -> figure boot target dependancies and activate them

    units
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
    //shutdown now, in 2 secs
        sudo shutdown -h now
        sudo shutdown -h +2
    //restart
        sudo shutdown -r now
        sudo reboot
