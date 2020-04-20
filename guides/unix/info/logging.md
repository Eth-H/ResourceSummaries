# System Logging
    services/kernel/daemons write logs to /var dir
    syslog/rsyslog service sends info to sys logger (rsyslog newer/advanced version)
    syslogd/rsyslogd daemon
        waits for event msgs to occur and filter important ones
            may log/print/del msg
    less /var/log/syslog
        timestamp hostname app
    files maintained by sys logger
        /etc/rsyslog.d
            EG
                /etc/rsyslog.d/50-default.conf
                    #  Default rules for rsyslog
                    auth,authpriv.* /var/log/auth.log
                    *.*;auth,authpriv.none -/var/log/syslog                                             
                    #cron.* /var/log/cron.log                                            
                    #daemon.* -/var/log/daemon.log                                         
                    kern.* -/var/log/kern.log   
            selector -> action
    //manually log to syslog
        logger -s Hello

# logs by file
    kernel
        /var/log/dmesg
            boot-time sys logs info about the kernel ring buffer
                info like: hardware drivers, kernel information, status during bootup, ...
            //read
                dmesg
            resets every boot
        /var/log/kern.log
            logs the kernel information and events on your system and dmesg output
    authentication logging
        /var/log/auth.log
        system authorization logs
managing log files
    hard to manage log disk space and see newer logs
    //tool to manage and compress logs, run by cronjob/day
        logrotate
        /etc/logrotate.d
