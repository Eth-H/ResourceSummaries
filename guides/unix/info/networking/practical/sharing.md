# via ssh
//cp file local host to remote host
    scp myfile.txt username@remotehost.com:/remote/directory
//cp file remote host to local host
    scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
//cp dir local host to remote host
    scp -r mydir username@remotehost.com:/remote/directory

# rsync (remote synchronization)
    scp with more features
    checks in advanced if there is already data that you are copying to and will only copy over the differences
        can deal with network interrupts woithout recopying entire thing
     verifies the integrity of a file checksums
    v, h: output verbose, readable
    r: recursive into dirs
    z: compressed for easier/quicker transfer
    //Copy/sync files on the same host
        rsync -zvr /my/local/directory/one /my/local/directory/two
    //Copy/sync files local host to remote host
        rsync /local/directory username@remotehost.com:/remote/directory
    //Copy/sync files remote host to local host
        rsync username@remotehost.com:/remote/directory /local/directory
# Simple HTTP Server
    python -m SimpleHTTPServer
    serves at http://IP_ADDRESS:8000
# NFS (Network File System)
    allows a server to share directories and files with one or more clients over the network
    //join server as a client
        sudo service nfsclient start
        sudo mount server:/directory /mount_directory
    cant use fstab
        automount, amd (newer)
        when a file is accessed in a specified directory, automount will find and mount the remote server
# Samba 
    protocols that allow unix and win comms
        Server Message Block (SMB) protocol
        Common Internet File System (CIFS)
    Samba allows linux to use CIFS to share files and resources
    
    sudo apt install samba
    //setup shared dirs, access perms, ...
        /etc/samba/smb.conf
    //change pw
        sudo smbpasswd -a [username]
    //make shared dir
        mkdir /my/directory/to/share
    sudo service smbd restart
    //win access
        run or file manager path
            \\HOST\sharename
    //linux access
        smbclient //HOST/directory -U user
        //mount network share
            sudo mount -t cifs servername:directory mountpount -o user=username,pass=password
