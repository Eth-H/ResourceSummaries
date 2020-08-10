# setup
## normal install 
may or maynot work
    sudo apt install ruby
    //do not install gems with sudo (future problems)
    gem install bundler 
## normal install  for user
    sudo apt install ruby --user
    gem install bundler
    //add bundler under home dir to path
## or with rbenv
stops most problems
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
// gem
    //install packages globally
    sudo gem install bundler
//bundler package manager
#use
    //install packages locally
    //install from Gemfile
        bundle install
    //update dependances 
        bundler update
    //get outdated dependancies
        bundler outdated
