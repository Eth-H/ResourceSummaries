#sudo apt-get install clang nodejs python3 npm lua5.3 liblua5.3 maven
sudo pacman -S clang nodejs python npm lua maven
sudo pip3 install jedi
git clone https://github.com/Shadowsith/TheVimIDE/
cd TheVimIDE
./install.sh
#./install-neovim.sh
cd ./build
./java_install.sh
./javascript_tern_install.sh