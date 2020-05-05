//see running processes using the most resources
    top

# List running processes
        //less: scroll through, grep [processName]: find stuff, grep bash | grep -v grep: find stuff and ignore grep process
        ps auxf | {}
    //Print current user running processes, See more info: -u, See all processes (not only for your user): -ax, -o [processName]:,
        ps {}
        //get processes for all users
        ps auxf
    //deal with processes by name
        //get cmds PID
            pgrep [cmd] 
        //kill cmds instances
            pkill [cmd]

    //get parent id of current tty
        echo $PPID
        cat /proc/$PPID/comm
        cat /proc/$PPID/cmdline

    //process tree
        pstree
        pstree -p -h -s 2072 //show pids, highlight current process and its ancestors, parent process of specified


# Services 
    //See status of all services
        service --status-all
    //All
        systemctl list-unit-files --type=service
    //Stop service auto starting
        sudo systemctl disable [serviceName]
    //start:, stop:
        sudo service [serviceName] {}		

# signals
    //Kill process, -9: kill 
        kill -{signal} [PID]	
        //run command to get PID first
            kill -9 `lsof -t -u [userName]`

//Add space to run new jobs
    //Send paused task to the background
        bg
    //Bring paused task back to the foreground
        fg
//Stop all running processes
    halt

# cron table 
    //Schedule commands to run at regular time intervals
    //Open crontab to edit tasks
        crontab -u [user]  [filePath]
    //Can edit /tmp/crontab
        minute(0-59) hour(0-23) day(1-31) month(1-12) weekday(0-6) command
    //EG
        0,14,29,44 * * * * /usr/bin/example2
        runs /usr/bin/example2 at the 15-minute mark on every hour, every day. Make sure you add each new task on a new line.

# get info on running processes
## lsof
//lists all all files, including processes, sockets, ...
    // -p [processID]: Find out what files the process is using
    //-r: read access, -w: write access
    //-u [userName]: process owned by specific user, -u^[userName]: not owned
    //-t: just get process PID
        lsof {}
        
    //-i: Check for IPv files 
     //tcp:[portName], 4: IPv4, 6: IPv6
        lsof {} {}
        //EG get all tcp port 80 traffic 
            lsof -i tcp:80 -P -R
## fuser (file user)
//identify processes using files or sockets
//show which processes use the named files, sockets, or filesystems
    fuser -v


desktop specific
