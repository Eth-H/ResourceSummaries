# links
    https://www.digitalocean.com/community/tutorials/how-to-install-go-and-set-up-a-local-programming-environment-on-windows-10
    https://stackoverflow.com/questions/30295146/how-can-i-install-a-package-with-go-get
    https://golang.org/doc/code.html#Command
    https://stackoverflow.com/questions/54415733/getting-gopath-error-go-cannot-use-pathversion-syntax-in-gopath-mode-in-ubun

# terms
    package: collection of source files in same dir compiled together
    module: collection of packages
    go.md
        declares module path for current project and requried dependancy modules

# setup
    export GOPATH="$HOME/go"
    export GO111MODULE=on

# workspace
    src: contains Go source files
    bin: contains exes built and installed by the Go tools (either your compiled source or downloaded files)

# setup local workspace (module)
    go mod init [projName]
    //install packages
        go mod download repo@version
    //download and install pkgs
        //save to to $GOPATH/src/<import-path> and run go install
        //dependancy modules from local go.mod
            go get
        //a specific module
            go get [moduleName]
        //only download, useful to make locally changes before installing
            go get -d [moduleName]


    //compile and install pkgs and dependancies
        go install
    //Eg
        go mod init example.com/user/hello
        //install your pkg
        go install example.com/user/hello
