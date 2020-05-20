#track
## top
    line1
        uptime cmd
        current time, sys runtime, num users lodded in, sys load avg
    line2
        tasks running, sleeping, stopped, zombied
    line3
        cpu info
            % CPU time spent
                us (user CPU time): running users processes that aren’t niced
                sy (system CPU time): running the kernel and kernel processes
                ni (nice CPU time): % running niced processes
                id (CPU idle time): spent idle
                wa (I/O wait): waiting for I/O. If Low, the problem probably isn’t disk or network I/O
                hi (hardware interrupts): serving hardware interrupts
                si (software interrupts): serving software interrupts
            st (steal time): CPU time stolen by other tasks from a running VM (if there is one)
    4th and 5th line: Memory Usage and Swap Usage
    processes list that are currently in use
        PID: process id
        USER: owner user
        PR: priority
        NI: nice value
        VIRT: virtual memory in use
        RES: Physical memory in use
        SHR: shared memory
        S: status of the process: S=sleep, R=running, Z=zombie,D=uninterruptible,T=stopped
        %CPU: %CPU used
        %MEM: %RAM used
        TIME+: total time of activity
        COMMAND: name
    //specify pids
        top -p 1

## lsof (list open files)
    lsof .
    //since every thing on linux is a file, lists alot
    //give associated processes to each file
## fuser (file user)
    fuser -v
## process threads
    lightweight processes
    process with 1 thread: single-threaded, >1: mulit-threaded
    processes operate with isolated sys resources, threads can share
    //view
        ps m
# mointor cpu
    uptime
        load average field
            avg cpu load in 5 10 15 min intervals
            %CPU full of traffic (processes waiting to load)
            1 load avg per core
# i/o monitoring
## cpu and disk useage
    iostat (from sysstat pkg)
        %CPU utilization
            %user: occurred while executing at user level (application)
            %nice: occurred while executing at the user level with nice priority.user CPU utilization with nice priorities
            %system: occurred while executing at the system level (kernel)
            %iowait: time that the CPU/CPUs were idle during with system outstanding disk I/O requests
            %steal: time spent in involuntary wait by the virtual CPU or CPUs while the hypervisor was servicing another virtual processor
            %idle: CPU or CPUs were idle and the system did not have an outstanding disk I/O request

        tps: Indicate the num of transfers (I/O reqs, of indeterminate size) /sec issued to the device. Multiple logical reqs can be combined into a single I/O request to the device
        kB_read/s: amount of data read from the device in kilobytes/sec
        kB_wrtn/s -amount of data written to the device in KB/sec
        kB_read - total num of KB read
        kB_wrtn - total num of KB written

# memory monitoring
    vmstat
        procs
            r, b: number of processes - for run time, in uninterruptible sleep
        memory
            swpd - amount of virtual memory used
            free - amount of free memory
            buff, cache - amount of memory used as - buffers, cache
        swap
            si, so: amount of memory swapped - in from disk, out to disk
        io
            bi: amount of blocks received in from a block device
            bo: amount of blocks sent out to a block device
        system
            in, cs - number of - interrupts/sec, context switches/sec
        cpu
            us, sy, id, wa: time spent in - user time, kernel time, idle, waiting for io

# continuous monitoring
    sar (from sysstat)
        /etc/default/sysstat 
            change ENABLED field (if not automatic)

        //list the details from the start of the day
            sudo sar -q
        //list the details of memory usage from the start of the day
            sudo sar -r
        //list the details of CPU usage
            sudo sar -P
        //view a different day
            sar -q /var/log/sysstat/sa02
# cron jobs
    create cronjob by ediring crontab file
        crontab -e
    syntax
        Minute (0-59), Hour (0-23), Day of Month (1-31), Month (1-12), Day of wk (0-7), <scriptName>
        30 08 * * * /home/pete/scripts/change_wallpaper

