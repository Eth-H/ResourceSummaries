# from source
## build
    //get source
      vi /etc/apt/sources.list
        //add debian backports as deb and deb-src
      aptitude update
      //find package
        apt-cache linux-source-5.4
      //install source locally (includes debian patches)
      apt source Linux-source-5.4
    //get kernel config 
      cp /boot/config-[version]-generic [kernelSource]/.config

    cd /path/to/linux-[ver]/
    patch -p1 < /path/to/filename.patch
    cp /boot/config-4.14.0-1-amd64 .config
    vim .config
        //delete
        CONFIG_SYSTEM_TRUSTED_KEYS=
    make oldconfig
    make -j8 deb-pkg LOCALVERSION=-custom
##### install
    cd ..
    dpkg -i *.deb


