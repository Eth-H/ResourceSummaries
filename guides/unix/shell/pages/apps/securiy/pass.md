# pass

> console password manager

## setup
    gpg --gen-pair
    pass init gpgPrivateKeyID
    //git setup
        pass git init
        //Initialized empty Git repository in /home/zx2c4/.password-store/.git/
        pass git remote add origin kexec.com:pass-store

## search
- list folders
    pass ls [subfolder]?
- list pw names close to pwname
    pass find [pwName]
- search pw-files containing sQ
    pass grep [searchQuery] {}?
    
    pass -c [pwName]
    pass [pwName]
    //EG
        pass Email/zx2c4.com

## edit store
    
    pass insert [pwName]
- multiline entry

        pass insert -m [pwName]
- remove existing password or directory

    pass rm {--recursive, -r; --force, -f;} pass-name
- renames or moves old-path to new-path

    pass mv {--force,-f} [old-path] [new-path]                          

- edit password txt file in vim

    pass edit [pwName]

## gen pw
    //-c: output to clipboard, -i: output inplace 
    //-f: force overwrite
        pass generate {}?... [pwName] [pwLength]
