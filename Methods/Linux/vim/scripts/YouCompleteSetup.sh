#run me after setting up vim
#custom settup required to get autocomplete for certain languages
sudo pacman -S cmake
cd ~/.vim/bundle/YouCompleteMe/
#use -h to get commands for individual languages
python3 ./install.py --all


#can also build before running :PluginInstall via cloning https://github.com/ycm-core/YouCompleteMe#installation