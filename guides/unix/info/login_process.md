init system will start the login process
    terminal getty/login
        run xserver -> run .xinitrc and .xsession or default sys wide .xsession
        after pw authentication execs a interactive login shell
            
            first argv[0] char will be a - followed by a shell, echo $0 = -bash
            will run ~/.profile, ~/.bash_profile
                export env vars
    graphical login / display manager
        after auth will exec interactive non-login shell
