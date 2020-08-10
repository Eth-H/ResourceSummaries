# Services 
## sysv legacy
- See status of all services
    
    service --status-all

- start/stop/restart a service
    
    sudo service [serviceName] start/stop/restart
    
- list services, will only show top services (EG dbus not dbus.x.service)

    service --status-all

## systemd

> modern init system
> /usr/lib/systemd/system/: units provided by installed packages
> /etc/systemd/system/: units installed by the system administrator

- list units
    
    systemctl list-unit-files

    - just daemons
        
        systemctl list-unit-files --type=service
    
    - active

        systemctl --type=service --state=active
    
    - active and running

        systemctl --type=service --state=running

- start/stop service auto starting

    sudo systemctl enable/disable [serviceName]

- list failed
    
    systemctl --failed

- reload
    - specific unit and its config

        systemctl reload unit

    - systemd manager config

        systemctl daemon-reload
