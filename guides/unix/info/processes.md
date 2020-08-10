# read processes
## ps
    PID: Process ID
    TTY: Controlling terminal associated with the process
    STAT: Process status code
        R: running/runnable, waiting for the CPU to process it
        S: Interruptible sleep, waiting for an event to complete, EG waiting for stdin
        D: Uninterruptible sleep, cannot be killed or interrupted with a signal, usually to make them go away you have to reboot or fix the issue
        Z: Zombie
        T: Stopped
    TIME: Total CPU usage time
    COMMAND: Name of executable/command

    //a: all users processes running, u: more details, x: processes that don't have a associated TTY (has a ?)
    ps aux
        USER: effective user 
        %CPU: CPU time used divided by runtime
        %MEM: Ratio of the process's resident set size to the physical memory on the machine
        VSZ: Virtual memory usage
        RSS: Resident set size, the non-swapped physical memory that a task has used
        START: Start time

## top
    realtime info

# terminals
    tty (terminal devices)
        native terminal device, type into to send output to sys
    pts (pseudoterminal devices)
        emulate terminal
    most processes bound to terminals
    except daemon processes launched by init sys

# process details
    process: sys allocating process to make a program run, an instance of a running program
    kernel deals with processes and knows
        status, resources used and received, owner, signal handling, ...

## process creation
    when a new process is created existing process basically clones itself using the fork sys call
    identical child process has a new PID, parent gets PPID
        child can continue using parents program or launch a new one via a execve sys call (destroys mem management put in place and sets up new ones)

## Process Termination
    _exit sys call
        free up proccesses resources for reallocation
        terminates with a termination status
            0 = success
        parent needs to acknowledge child termination
            wait sys call check child termination status
    orphan processes
        when a parent process dies before a child process
        kernel makes them orphans and puts under init (PID 1)
            init will perform the wait sys call so they can die
    zombie processes
        when _exit called but not wait, kernels turns process into a zombie
            resources freed up, entry in process table
            cannot be killed
            parent calls wait (reaping occurs) and it disappears, or init sys adopts
# signals
    ways processes can communicate
    uses
        special terminal characters (Ctrl-C)/(Ctrl-Z) to kill/interrupt/suspend
        hardware/software issues can occur and the kernel wants to notify the process
    signal process
        events gens signal -(pending status)> delivered to process -> signal mask blocks or recevied
        actions
            ignore
            catch and perform a specific handler routine
            process can be terminated, as opposed to the normal exit system call
            block the signal, depending on the signal mask
        common signals
            SIGHUP/HUP/1: Hangup
            SIGINT/INT/2: Interrupt
            SIGKILL/KILL/9: Kill (unblockable)
            SIGSEGV/SEGV/11: Segmentation fault
            SIGTERM/TERM/15: Software termination
            SIGSTOP/STOP: Stop
        man [signalNum] signal

# kill
    send terminating signals
    //default SIGTERM
        kill PID 
    //specify signal
        kill -9 12445 
    //avaliable actions
        SIGHUP: Hangup, sent when the controlling terminal is closed
        SIGINT: interrupt signal, gracefully kill, Ctrl-C
        SIGTERM: Kill, but allow some cleanup first
        SIGKILL: Kill
        SIGSTOP: Stop/suspend

# niceness
    processes given cpu time slice, then pasued until their next one
    can influence kernel's process scheduling algorithm
        nice val: level of priority for a process, high = nice = lower priority
        //new process
            nice -n 5 apt upgrade
        //existing process
            renice 10 -p 3245

# /proc filesystem
    process info (everythings a file), how the kernel views the sys
    sub-dirs for every PID
    ps gets some info from /proc

# Job Control
    //send to background
        sleep 1000 &
    //view all bg jobs
        jobs
        +: most recent bg job that started
        -: 2nd
    //suspend
        Ctrl-Z
        //send it to fg/bg
            fg, bg
    //bring job back from background
        fg //most recent
        fg%1 //specify job id
    kill %1
