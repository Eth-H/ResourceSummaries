point
    owner of the process
    access permissions

groups: set of users that get the groups permissions

some daemons have a username acc

//get superuser access (run cmds as root)
    sudo, su
    //edit users/groups who can sudo
        /etc/sudoers

/etc/passwd
    UID/GID mapped to user/group name
    root:x:0:0:root:/root:/bin/bash
        Username
        User's pw - x: pw stored hashed in /etc/shadow, *: user doesn't have login access, blank: no pw
        UID:GUID
        GECOS field - comments about the, is comma delimited
        User's home directory
        User's shell - default bash
    
cat /etc/shadow
    root:MyEPTEa$6Nonsense:15000:0:99999:7:::
        username:encrypted pw
        date of last password changed - num days since jan 1, 1970, 0: user should change their pw the next time they login
    min pw age:maximum password age - in days
    pw warning period - num of days before a password expires
    pw inactivity period - num of days after pw expiry to allow login with their pw
    account expiration date - date user cant login
    reserved field for future use

PAM (Pluggable Authentication Modules) generally replaces /etc/shadow

/etc/group
    root:*:0:pete
roup name:Group password (generally uneccesary):GID:List of users

management
    when a new user is created a group is created for him
        sudo useradd bob
        //specify groupname
            sudo useradd -g WHEEL bob
        sudo userdel bob
        passwd bob
        //list groups for current process
            groups
        //for certain user
            groups user
        //create group
            groupadd
