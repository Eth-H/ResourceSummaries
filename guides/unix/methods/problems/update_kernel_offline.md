# problem
    network hardware wont work
    generally this is because kernel is outdated
    recomended to have anouther working machine with updated linux kernel 
    this tries to resolve without building a custom/patched kernel
    
# get packages 
## M1
    //Step 1: Get the download URLs in a file :
        apt-get -y install --print-uris <packagename> | cut -d\' -f2 | grep http:// > apturls
    //Step 2: Copy this file (apturls) to a machine with Internet access, and execute the following command to download the packages:
        wget -i path-to-apturls-file 
## M2
    //get from website
        wget -c <url>
        //http://debian.csail.mit.edu/debian/pool/main/l/linux-2.6/linux-image-2.6.32-5-486_2.6.32-39_i386.deb
        //http://packages.ubuntu.com   
## M3
    apt-add repository ppa:kernel-ppa/ppa
    apt-get update
    apt-get install PACKAGENAME
## M4
    //get from local machine (with right/new kernel)
        ls /var/cache/apt/archives | grep "*packagename*" 
        cd /var/cache/apt/archives
        find -name "*packagename*"

## install packages on target PC
    dpkg install <packageList>
    //if errors, try to resolve your dependencies 
    apt-get -f install

    //or with gdebi
        //Simple tool to install deb files - GNOME GUI gdebi lets you install local deb packages resolving and installing its dependencies. apt does the same, but only for remote (http, ftp) located packages.
        apt-cache show gdebi


