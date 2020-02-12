###Sys module
import sys
sys.exit() #Exit python.

#Other tools if the paths need to be joined	
#import os
#newUrl = os.path.join(url, filename)


# Browse directories> -------------------------
import os 
def Test1(rootDir): 
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        for d in dirs: 
            print os.path.join(root, d)      
        for f in files: 
            print os.path.join(root, f) 
Test1('/tmp/aliendir')
