# virtualenv
	mkdir ./venv
	//--python=/usr/bin/python3.6 --system-site-packages: inherit system packages
        virtualenv ./venv {}...
	cd ./venv
	source bin/activate
	deactivate
	//Export list of dependancies 
	pip freeze > requirements.txt
# pip
//install, unlock, lock
pip {}

# pipenv
## install
    pip install --user pipenv
    //temporarily add to path
        export PATH="$PATH:/home/emera/.local/bin"
    //add to path pernemantly
        cd /usr/bin
        sudo ln -s ~/.local/bin/pipenv
## use
    //setup a project/VE
        //Create pipfile and VE
            //--three: system py 3, --two: system py 2, --python [interpretorPath or specificVersion]:         
                pipenv {}
        //--run [commmandName]: run command in VE --shell: spawn shell in VE, generally use to initialise VE
            pipenv {}
        //EG initilise VE and chose python version
            pipenv --python 3.6 --shell
        
    //workflow
        cd myproject
        //       
            //none: If pip file exists install from it, converts requirements.txt if it exists
             //-r [path/to/requirements.txt]: Specify path, --dev: Install dev and default Pipfile packages            
            //[packageName]: Install package into local VE, create Pipfile if it doesnt exist
             //--system: Use system pip, accepts intialise VE params
            pipenv install {} {}
        //
            //pipenv install parameters, --all:, --all-dev:
            pipenv uninstall {}

        
        //Exit virtual environment (need to close current shell session)
            exit
    //Upgrade packages
        //none: all pkg, --outdated:, [pkgName]:,
        pipenv update {}

    //Dependancy graph
        pipenv graph

    //Locate
        //--venv: VE, --py: interpretor, --where: project
        pipenv {}
    //Instal package from git
        [vcs_type]+[scheme]://[location]/[user_or_organization]/[repository]@[branch_or_tag]#[package_name]
    //warnings
        //even if a packagefails to install, it may be added to pipfile and cause errors
