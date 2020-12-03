# pip
- install, unlock, lock

    pip {}
    pip -U //upgrade all pkgs
    pip install --upgrade pkg //upgrade a pkgs
    pip install --user --upgrade pkg //upgrade a pkg installed for a specifc user
    pip install -r requirements.txt
    pip list --outdated

# virtualenv
container for python pkgs
install python pkgs locally within a project
use in conjunction with pip
	mkdir venv
    #specific py version
    virtualenv ./venv --python=[pathToPythonExe]
    #inherit system packages
    virtualenv ./venv --system-site-packages

	source venv/bin/activate
	deactivate

# pipenv
## install
- will install to ~/.local/bin, may need to add this dir to path

    pip install --user pipenv

## use
- create pipfile and VE

    pipenv --python [2|3]
    pipenv --python [pathToPythonExe]
    #can also use any other pipenv cmd to initialise

- run command in VE 
    pipenv --run [cmd]
- spawn shell in VE
    pipenv --shell [cmd]

    - exit virtual environment (need to close current shell session)

        exit
## install stuff
    pipenv install [pkg]
- install a requirements .txt
    pipenv install -r requirements.txt
- install dev and default pipfile packages            
    pipenv install -d requirements.txt
- use system pip
    pipenv install --system

## uninstall

    pipenv uninstall [pkg]
    pipenv uninstall --all
    pipenv uninstall --all-dev
        
- upgrade packages
    - all pkg
    pipenv update {}
    - specifc pkg
    pipenv update --outdated [pkgName]
- dependancy graph
    pipenv graph

- locate
    //--venv: VE, --py: interpretor, --where: project
    pipenv {}

## other
- Instal package from git
    [vcs_type]+[scheme]://[location]/[user_or_organization]/[repository]@[branch_or_tag]#[package_name]
- warnings
    - even if a packagefails to install, it may be added to pipfile and cause errors
