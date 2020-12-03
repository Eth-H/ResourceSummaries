# setup
## normal install 
may or maynot work
    sudo apt install ruby
    //do not install gems with sudo (future problems)
    gem install bundler 
## normal install for user
    sudo apt install ruby --user
    gem install bundler
    //add bundler under home dir to path
## install pkgs with user
this will install pkgs under user rather than system wide
    sudo apt install ruby
    gem install --user-install bundler
    bundle config set path $HOME/.gem/

## rbenv
have multiple ruby installs, stops most problems
    git clone https://github.com/rbenv/rbenv.git ~/.rbenv
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc
    exec $SHELL
    git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
    echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
    exec $SHELL
    //install a version
    rbenv install 2.7.1
    //set a ruby version for the local dir (and subdirs)
    rbenv local 2.7.1
    //set ruby version for entire system
    rbenv global 2.7.1
    //run after installing gems
    rbenv rehash
    //can which ruby versions gems under
    ~/.rbenv/versions/<ruby-version>/lib/ruby/gems/..

# gem pkg manager
    //env vars
        gem env
    // list
        gem list

# bundler local pkg manager
    //install packages locally
    //install from Gemfile
        bundle install
    //update dependances 
        bundler update
    //get outdated dependancies
        bundler outdated
