//check download source hash
    md5sum -c md5sums_file
//check signitures
    gpg --import {public-key}
    gpg --verify sign.[gpg|sig|asc]

    tar -xf filename
    //above individually
        gzip -cd filename.tgz | tar xf -
        bunzip2 -cd filename.tar.bz2 | tar xf -
    //avoid
        -C or --directory
        -P or --absolute-names
        --transform or --xform
    //check an archive before extracting
        tar -tf filename
// read
    README
    INSTALL //pre-requist libs/programs
// apply patches if neccessary
    // sed/awk scripts or patch file

// build systems
    ./configure //sh script to use makefile.in to gen a makefile
    //makefile.in

    //may be used instead of configure
    cmake . -DCMAKE_BUILD_TYPE=Release {some options ...}
    //configure may require some env vars
    NAME=tom ENABLE_FOO=no ./configure

    //unqiue syntax, list of rules of the form: when TARGET-FILE is older than SOURCE-FILE then SOME-ACTION
    //locally compilesp program
    make

    //install globally
    sudo make install

    //clean compiled files
    make clean

// help pages
    man
    info
    html pages

// makefile syntax
    target: dependency1 [dependency-n ...]
    <tab> command to execute
    ...
