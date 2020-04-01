//note: throughout use can redirect (>) or pipe (|) outputs rather than using -o
# setup	
    sudo apt-get install gnupg
# manage keys
    //generate key, choose needed algorithm and keysize (bigger for more security), no expiry, 
     // then enter name/email/comment, enter password for private key
     //note real name, key-id (last part (8) of fingerprint), key fingerprint (40 digits)
        gpg --gen-key
    //--list-keys: list keys, --list-public-key: list public keys, --list-secret-keys: list private keys
        gpg {} [specificKeyIDorName]?
    //Give public key to someone else
        //export public key (raw data is converted to armoured ASCII) for others
            gpg --armor --export Tutonics > publicKey.asc
## import a friends pub key 
    gpg --import friendsPublicKey.asc
    //validate imported key
        //enter gpg cli
            gpg --edit-key [keyName]
        //display finger print
            fpr
        //once verified sign using sign
            sign
        //double check its signed
            check
        // optionally can trust a signiture if you know the owner, enter 5 (I trust ultimately)
            trust
        //exit cli
            q, CTRL + d
## move your private key	
    //export private key
        gpg --export-secret-keys [key-id] > privateKey
    //import private key on other machine	
        gpg --import privateKey	
        //use a keyserver
            //store key on KS
                gpg --keyserver [KSname] --send-keys [key-id]
            //recevie key
                gpg --keyserver [KSname] --recv-keys [key-id]
## Revocate key		
    //Create revocation cert using private key
        gpg --output [revocationCertName].asc --gen-revoke [key-id]
    //Use revocation cert
        gpg --import [revocationCertName].asc
        gpg --keyserver [KSname] --send-keys [key-id]

# asymmetric encryption
    //encrypt with pub key, decrypt with private key
    //encrypt file
        gpg -o [encryptedFileName].gpg -e -r [key-id] [filename]	
    //decrypt, the passphrase for the private key is needed
        gpg -o [decryptedFileName] -d [encryptedFileName].gpg
        
## Digital signitures (to identify tampering)
### desc
    //sender generates hash of data -> hash encrypted with sender priv key and added to original data -> optionally then the're encrypted with recipients pub key -> if encrypted recipient decrypts with priv key 
    // -> digital signiture is decrypted using senders pub key to reveal the original data's hash -> recipient re-calculates hash and if it matches then the integrity of the owner and data is proved. 
### use 
    //create signiture
        //normal signiture: raw binary data of the signature is included with the original data
        //clearsign signiture: Signiture is added as a base64 ascii-armour
        //--sign, -s: normal signiture, --clearsign: clearsign signiture
         //-o [signedFileName]: default signed file name is [fileName].asc but can control output
         //--local-user [userName]: sign using anouther private key
            gpg {} {}? [fileName]	
        //default signed file name is [fileName].asc, control output
            gpg -o [signedFileName] --clearsign [fileName]
        //sign and add asymmetric encryption
            gpg -o [signedFileName].enc -s -e -r [key-id] [fileName]
    //verify signiture								
        //verify on recipient pc using senders public key, even if its encrypted it will verify the signiture (but the msg wont be decrypted)
            gpg --verify [signedFileName]
        //To decrypt and verify can use just decrypt as it automatically tries to verify present signitures
            gpg -o [fileName] -d [signedFileName].enc
    //Detach signiture to crate .sig file
        gpg --detach-sign [signedFileName]
    //Can still verify original file if its within the same dir, otherwise append path 
        gpg --verify [fileName].sig [pathTo fileName.txt]?
            
//symmetric encryption
    //pub key used to encrypt and decrypt
    //default gpg uses cast5: gpg <2, aes128: gpg >2.1
    //to change default  edit ~/.gnupg/gpg.conf and add: cipher-algo [algorithmName]

    //-c, --symmetric: symmetric encryption
     //--cipher-algo: [algorithmName], -o [fileName]: specify output fileName, default is [fileName].gpg, --force-mdc: if using <64 bit cipher use this to prevent message modification atks
     //--armour: ascii armoured text (produces .asc file for default name)
     //-s: sign data before encryption	
        gpg {} {}?... [filePath.txt]
    //eg
        gpg --armor --symmetric --cipher-algo AES256 file.txt
    //Decrypt, pw required
        gpg -o [filePath].txt -d [fileName].gpg
    

# check a linux distro checksum for validity
    //check if key already installed
        gpg --keyid-format long --verify SHA256SUMS.gpg SHA256SUMS
    //if key not installed use RSA key prefexed by 0x, and request matching public key from a keyserver
        //ubuntu
            gpg --keyid-format long --keyserver hkp://keyserver.ubuntu.com --recv-keys 0x46181433FBB75451 0xD94AA3F0EFE21092
            //inspect keys
            gpg --keyid-format long --list-keys --with-fingerprint 0x46181433FBB75451 0xD94AA3F0EFE21092
    //verify
        gpg --keyid-format long --verify SHA256SUMS.gpg SHA256SUMS
    //check sums
        sha256sum -c SHA256SUMS 2>&1 | grep OK

## links
https://linuxconfig.org/how-to-verify-an-authenticity-of-downloaded-debian-iso-images
https://www.debian.org/CD/verify
https://keyring.debian.org/
https://superuser.com/questions/622541/what-does-dd-conv-sync-noerror-do
https://medium.com/@tbeach/use-unix-dd-command-to-os-bootable-on-usb-drive-6671945d95a6
