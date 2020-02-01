# Windows command line
## Directories and files
    //Change drive 
        D:	or	cd /D C:\Windows
    //Get directory details, /A: show hidden files
        dir {}
    //Display contents of a file one page at a time
        dir "c:\Windows" | more
    
## Edit directories and files
    //Make directory
        mkdir {[pathname]}
    //Copy
        //Copy just files
            copy [fileSourcePath] [directoryDestinationPath]
        //Copy multiple files EG
            copy *.txt [folderDestinationPath]
        //Copy anything, /s: Copy entire directory tree, /e: Copy empty directories 
            robocopy [folderSourceParh] [directoryDestinationPath] {}
        //Get help
            robocopy /?
    //Move anything
        move [sourceParh] [directoryDestinationPath]
    //Delete files
        del [filePath]
        del *.txt
    //Delete directories, command will fail if directory is not empty /S: override empty condition
        rmdir [directoryPath] {}
    //Rename stuff
        ren [pathOne] [pathTwo]	

## Search files>
    //Search files for text strings, hide error msgs
        find C:\Users\User\* "hello" 2>nul		
    //Get file path (linux which command), /R: Display a directory
        where [fileName] {}
# Fixing computer>
    Check win activation key
        wmic path softwarelicensingservice get OA3xOriginalProductKey    
    check disk
        chkdsk
        wmic diskdrive get status
        sfc /scannow
    //check drivers
        verifier
# Network
    //Get info, /all: more info, 
        ipconfig {}
    //Setting IP 
        netsh interface ip set address [connection name] static [IP] [subnet] [gateway]
    //Access files stored on a network
        //List commands
            net {[commandName]} /?
        //Mount a network drive
            net use x: \\DESKTOP-3VSCDO9\Share
        //Remove mounted drive
            net use x: /delete
        //See network connections
            netstat
            //See open ports
            netstat -a -b -o
# User management
    //View current users
        net user
    //Add user, enter * inplace of PW to enter it in the next work
        net user /add [username] [password]
        net user /delete [username]
    //View groups
        net localgroup
    //Check current user group memebership
        net user [username]
    //Add a user to a group
        net localgroup [groupName] /add [userName]
