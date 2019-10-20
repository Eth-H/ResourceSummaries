#!/bin/bash
sudo pacman -S gvim
sudo pacman -S lang nodejs python npm lua maven
#sudo apt-get install clang nodejs python3 npm lua5.3 liblua5.3 maven
sudo pip3 install jedi flake8

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
cp ./vimrc ~/.vim/vimrc
ln ~/.vimrc ~/.vim/vimrc
vim +PluginInstall +qall

echo "dont forget to install / update YoucompleteMe"
echo "https://github.com/j1z0/dotfiles.git"


