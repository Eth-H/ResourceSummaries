# xfce4-terminal

> run a terminal emulator window on xfce4 desktop env, most other TEs are similar

- open new terminal windows and execute command

xfce4-terminal -e: [commandName]

- open new tab, to run command in new tab pass it afterwards

xfce4-terminal -e mocp --tab -e mc

- specific window size

xfce4-terminal --geometry 80x40 -e mocp --tab -e mc

- exit with exit status of last run program

    exit
- exit with specific exit status

    exit {unixExitCode}
