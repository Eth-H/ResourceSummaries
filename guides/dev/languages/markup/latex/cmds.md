texlive pkg manager
    //setup
    tlgmr init-usertree
    //lsit repos
    tlmgr repositary list
    //set main repo
    tlmgr option repository http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2019/tlnet-final
    tlmgr option repository http://mirror.ctan.org/systems/texlive/tlnet
    //dont check signitures on install
    tlmgr --verify-repo=none install adjustbox

//update fonts for usr or sys
    updmap -usr
    updmap -sys


https://tug.org/texlive/scripts-sys-user.html
https://www.ctan.org/
    anorien.csc.warwick.ac.uk
    mirror.ox.ac.uk
