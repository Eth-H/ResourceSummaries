java 
    //archlinux java management
        //status: list all installed java JDKs, set [javaFromStatus], fix: fix invalid jre links
        archlinux-java {}
        //EG java-11-openjdk/bin
            archlinux-java set java-8-openjdk
        //run program with a different java version
        #!/bin/sh
        export PATH=/usr/lib/jvm/java-8-openjdk/jre/bin/:$PATH
        exec /path/to/application "$@"	
    

