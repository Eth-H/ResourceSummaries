# links
    https://www.atlassian.com/git/tutorials/comparing-workflows
    https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase
    https://www.atlassian.com/git/tutorials/merging-vs-rebasing
    https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting

"//"
"" instructions
"->" Process
"//(x)" Declaration of Index "x"
"{x}" Reference to index "x"

# git concepts
## how it works
    Git is the version control system that runs locally on your PC, GitHub.com is a hosting website that saves files. To go past saving files a link between the local repo and online GitHub repo needs to be established
    Git to GitHub: A repo is created (a file system is marked as a repo) -> you set files to be tracked (changes to these files are saved by git) -> Established local repo to online repo connection 
     -> Tracked files are staged to be pushed (commited) -> staged pushed up to the remote repo 
    GitHub to Git: Establish online repo to local repo connection -> pull repo down locally -> changes to current files are tracked and new files added are tracked -> commit changes -> push changes
    Cloning a repo: This means to pull someone elses repo down locally, you can do this to copy remote repositaries to edit it locally as your own, though you would need permission to push chanegs to the original 

## components/elements
    git repo: comprised .git and working tree
    .git dir: configs,logs,branches,head,...
    working tree: dirs and files in working dir (pwd)
    index: stageing area in .git, separates working tree from git repo
    commit: snapshot of changes to the working tree
    branch: pointer to the last commit, updates with new commits
    tag: mark on specific history point, mark releases
    HEAD: pointer to current branch, only 1 active HEAD
    head: pointer to any commit, can have multiple
    stages:
        modified: workind dir changes but not includeded in .git db
        staged: marks file for commit
        commited: files commited to .git db

## terms
    conflict:
        top of repo is behind remote counterpart
        if one persons commits to the central repo, then anyone else who cloned before he pushed changes wont have the latest updates, hence they wont be able to push changes and will need to pull and integrate the remote changes with ther local branch

## git state
    git has 3 ways to manage its state
    the working dir (local filesystem)
    staged snapshots (commits)
    commit history
    

## basic workflow
    //create own repo
        create github repo -> clone -> add files to tracking/staging and commit changes -> push changes 
                      //or -> init -> connect to remote -> add/commit/push
        
    //pull request someone elses repo
        fork -> clone -> create feature branch -> add files to tracking and commit changes -> push feature branch to fork -> go to original repo and hit pull req (from your branch)

## configure account (for current machine)
    git config --global user.name "Firstname Lastname"
    git config --global user.email username@email.com
    git config --global core.editor Vim
    git config --global user.signingkey [keyID]
    git config --global grep.lineNumber true
    //edit all
    git config --global --edit
    //check
    git config --global --list
    //alias
        git config --global alias.st status
        git config --global alias.ci commit
        git config --global alias.br branch
        git config --global alias.co checkout
        git config --global alias.df diff
        git config --global alias.lg "log -p"
        git config --global alias.g "grep --break --heading --line-number"
## quick setup
    mkdir projroot && cd projroot
    git init
    git add .
    git add LICENSE
    git add README
    echo node_modules > .gitignore
    git commit -m "initial commit"
    git remote add origin [repoUrl]
        //if externel repo has unrelated history
            git pull origin master --allow-unrelated-histories
            git merge origin origin/master
            git push origin master

## clone
    git clone [repoUrl] rootdirname
- shallow clone - faster cloning that pulls only latest snapshot

    git clone --depth 1 https://github.com/adambard/learnxinyminutes-docs.git

- clone only a specific branch

    git clone -b master-cn https://github.com/adambard/learnxinyminutes-docs.git --single-branch

## commit files
stage files to be pushed up to the actual repo
    //add files to staging area for commit
    git add .
    git commit 
    //optional commit message
    git commit -m "Fix this thing"
    //ignore staging area (no git add)
    git commit -a 
    //change last commit
    git commit --amend -m "Correct message"

## remote
    //list
        git remote -v
    //add
        git remote add [repo]
        git fetch
    //rm conn
        git remote rm
    //rename
        git remote rename
    //show additional info
        git remote info
    //change remote
        git remote set-url

### pushing updates
moving files locally to online repo, origin: default name of remote connections
    git push [remote] [branch]
    //fix conflict problems
        git push origin master --allow-unrelated-histories
        git push origin master -f
    //Push wthout origin link
        git push https://[username]@github.com/[github repository] [local branch name]:[remote branch name]

### pull repositories
pull online github repo locally
    git pull [repoUrl]
    git pull [remote] [branch]
    //pull repo and commit history, then integrate with local commits (needed if top of repo is behind remote counterpart)
        git pull --rebase origin master
#### fetch 
get branches and tags
```sh
git fetch

#fetch all the branches simultaneously
git fetch -all
#synchronize the local repository
git fetch origin
```

#connect to repo via ssh
    ssh user@host git init --bare /path/to/repo.git

## commit history
summary of recent commits, head status
```sh
# all commits
git log
    #last 2 commits
        git log -2
    # with path
    git log -p -2

# just commit msg and ref
git log -oneline
# Show merge commits only
git log --merges
# Show all commits represented by an ASCII graph
git log --graph

#modified files
git log -stat
    #with location
    git log -p
git log --diff-filter=D --summary


#modification of each line of a file and who
git blame [file]
```

### undo stuff
```sh
    #discard local chnages in cwd
    git reset --hard HEAD
    #discard changes in a file
    git checkout HEAD [file]
    #reverse commit
    git revert [commit]
```

## track changes
```sh
#diff between working dir and index
    git diff
#diff between index and last commit
    git diff --cached
    #or
    git diff --staged
#diff between cwd and last commit
    git diff HEAD
#track the changes between two commits
    git diff Git Diff Branches:
    git diff < branch 2>
#status of pwd and staging area
    git status
#show objs
    git show
```

## branching
```sh
#list all branches, without/with remote
git branch --list
git branch -a
#list current branch
git branch
#del locally/remote
git branch -d [branchName]?
git push origin -delete [branchName]?
#mv/rename
git branch -m [oldBranchName]? [newBranchName]
```

### checkout
mv head ref pointer to a specified commit
    update files in the working tree to match a index version or specific tree
    change contents of file to a specified commit
    change branch: update index and files in working tree, point HEAD at branch
```sh
#create branch and switch, dont use if branch already exists
git checkout -b [branchName]
#switch branch
git checkout [branchName]
#merging (merge branch to active branch)
git merge [develop] --no-ff
#commit to remote branch
git push origin -u 'branchName'
```
### stash
switch branches without committing the current branch
save dirty cwd state as a stack of reapplyable unfinished changes
```sh
#stash current changes
git stash
#saving stashes with a message
git stash save ""
#check the stored stashes
git stash list
#re-apply the changes that you just stashed
git stash apply
#track the stashes and their changes
git stash show
#re-apply the previous commits
git stash pop
#delete a most recent stash from the queue
git stash drop
#delete all the available stashes at once
git stash clear
#stash work on a separate branch
git stash branch 

#EG use
    #dirty cwd, need to pull changes
    git stash
    git pull
    git stash list
    git stash pop
```
### cherry pick
    //apply changes from a specifc commit
        git cherry-pick

## merging
integrate changes of one branch into anouther
creates merge commit in featureBranch that ties together histories of both branches
adv/disadv: does not change existing branches, adds extraneous upstream commit that pollutes history
```sh
#merge branches or a specified commit
git merge featureBranch upstreamToMergeBranch
#or
git checkout featureBranch
git merge upstreamToMergeBranch
```
### rebase
integrate changes of one branch into anouther
mvs featureBranch to begin at the tip of the upstream branch
EG rebase featureBranch onto upstreamBranch
    saves featureBranch commits to buffer, copies upsteamBranch into its place
    then rewrites copied upstreamBranchs history with brand new commits for each commit in the featureBranch
adv/disadv: clear and linear history (easy to navigate), loses merge commit context (cant see where upstream changes incorporated into feature)
golden rule: never rebase public upstreamBranch onto featureBranch (cant rewrite history of a public branch)
```sh
#apply a sequence of commits from distinct branches into a final commit
git chechout featureBranch
git rebase upstreamToMergeBranch
#or
git rebase featureBranch upstreamToMergeBranch

#continue/abort rebasing process after merge failure
git rebase -continue
git rebase --skip

#interactive rebase: allow edit, rewrite, reorder, ..., on existing commits
git rebase -i

#cleanup feature branch, allows to code without isolated commits and clean up later, EG re-write the last 3 commits
git checkout feature
git rebase -i HEAD~3
```

## ignore files
    // line start comment: "#", start with / to ignore recursivity, end with / to avoid a directory, negate a patturn by starting with an exclamation mark
    vim .gitignore
        *.[oa]
        *~
## undo

### clean
    remove untracked files from working tree
    git clean

### revert
undo a commit, via adding a new commit that undos the old one
    git revert [targetCommit]?

### reset
reset current HEAD to specific state. Can undo merges,pulls,commits,adds,...
```sh
#reset staging area to latest commit, leave cwd
git reset
git reset 31f2bb1

#above but overwrite cwd (to match), will delete commits
git reset -hard
git reset -hard 31f2bb1



git reset -soft:
git reset --mixed
```
### reflog
list git cmds over tiem period, default 90 days
can reverse with git reset
```sh
git reflog
git reset -hard 31f2bb1
```


## mv/rm files
```sh
git mv HelloWorld.c HelloNewWorld.c
#force overwrite
git mv -f myFile existingFile

#from fs and git (untrack)
git rm [fn]?

#just from git
git rm --cached [fn]?

#untrack .gitignore  files
git rm --cached `git ls-files -i --exclude-from=.gitignore`
#or
git ls-files -i --exclude-from=.gitignore | xargs git rm --cache

#untrack and del
git rm log/\*.log
git rm \*~S
```

## tags
```sh
# ls
git tag
#create
git tag -a v2.0 -m 'my version 2.0'
#tagger info, commit tag date, annottion msg, commit info
git show v2.0
#push a single/lots tag to remote
git push origin v2.0
git push origin --tags
```

## grep
```sh
# search for "variablename" in all java files
git grep 'variableName' -- '\*.java'

# search for a line that contains "arraylistname" and, "add" or "remove"
git grep -e 'arrayListName' --and \( -e add -e remove \)
```

# other cmds
    git show "file"

# problems
## contribute to open source repo
//fork repo on github
git clone https://github.com/YOUR_USERNAME/GitMe.git and cd GitMe
git checkout -b username-feature
//make changes
git add .
git commit -m "cmt msg"
git push -u origin username-feature
//make pull request

## forked a repo and need to get new changes from upstream repo
- add the original repo as upstream remote and fetch refs
git remote add upstream https://github.com/user/forked-repo
git fetch upstream

- fetch+merge like a git pull
git merge upstream/master master
- or, replay your local work on top of the fetched branch, like a "git pull --rebase"
- make sure you are in the branch you want to rebase if you dont specify a 2nd branch
git rebase upstream/master

- update fork
git push -f origin master


## want a file deleted in a previous commit
    //find commit
        //summaries
        git log
        //diff introduced in each commit, last 2 commits
            git log -p -2
        git log --diff-filter=D --summary

    //revert to older commit with file
        git checkout [commitId] 

## reverse file to last commit
    git log path/to/file
    git log -p path/to/file
    //use commit with wanted version of file
    git checkout <commit> path/to/file

## Head is checked out problem
    //Create new branch and re-attach HEAD to it
    git checkout -b temp
    
    //Check differences between branches before continuing
        git log --graph --decorate --pretty=oneline --abbrev-commit master origin/master temp
        git diff master temp
        git diff origin/master temp
    
    //Update master branch to point to the new branch
        git branch -f master temp
        git checkout master
    //Push it
        git push origin master
## Remove folder from local git and remote 
    git filter-branch --tree-filter 'rm -rf node_modules' --prune-empty HEAD
    git for-each-ref --format="%(refname)" refs/original/ | xargs -n 1 git update-ref -d
    echo node_modules/ >> .gitignore
    git add .gitignore
    git commit -m 'Removing node_modules from git history'
    git gc
    git push origin master --force
## remove folder from repo but not local
    git rm -r --cached FolderName
    git commit -m "Removed folder from repository"
    git push origin master
    
# git workflow in industry
## centralized workflow
    uses a central repository to serve as the single point-of-entry for all changes to the project		
    process: clone central repo -> commit changes but store locally isolated -> push local master branch at breakpoint	
    conflicts 
        since history is all focused on one branch, rebasing new commits on top of remote changes is a good idea
            git pull --rebase origin master
            //this rebases the local master branch ontop of the origin/master branch
        if conflicts while rebasing
            //conflict (content): merge conflict in [some-file]
            //find unmerged paths
                git status
            //edit files then stage and rebase
                git add [problematicFile]
                git rebase --continue
                //If the rebasing goes wrong can go back to start
                    git rebase --abort
## git feature branch workflow
    still uses one central repo, but features developed in their own branches
    if each dev works on their own branch, this allows changes to be stored serverside
    process: clone central repo -> create feature branch -> push feature branch as remote tracking branch -> when done create pull req to merge feature branch into the master/dev branch

    //start with master branch
        git checkout master
        git fetch origin
        git reset --hard origin/master
    //create branch
        git checkout -b [branchName]
    //after commits push feature branch to remote, -u: setup tracking branch, not can use "git push" to push new branch to central repo=
        git push -u origin [branchName]
    //make a pull request with git GUI (for code review)
        //if accepted merge with master branch	
        git checkout master
        git pull
        git pull origin [branchName]
        git push
        git merge BranchName //or id merge conflicts
## gitflow workflow
    suited for projects that have a scheduled release cycle
    uses two branches to record the history of the project. The master branch stores the official release history, and the develop branch serves as an integration branch for features.

    //create dev branch
        git branch develop
        git push -u origin develop

        //feature branches use develop as their parent branch
         //create a feature branch
            git checkout develop
            git checkout -b feature_branch
        //Merge feature branch
            git checkout develop
            git merge feature_branch
        
        //Once develop has acquired enough features for a release, you fork a release branch off of develop, this allows for the team to work on current and future releases
            git checkout develop
            git checkout -b release/0.1.0
        //once release is ready to ship merge to master and develop
            git checkout master
            git merge release/0.1.0
        //use a hotfix branch to quickly patch production releases, similar to new feature branches but they focus on master instead of development
            git checkout master
            git checkout -b hotfix_branch
            //after changes merge to master and develop
                git checkout master
                git merge hotfix_branch
                git checkout develop
                git merge hotfix_branch
                git branch -D hotfix_branch
            
        //could use dev-flow library (install git-flow with apt or brew )
            git flow init
            git flow feature start feature_branch
            git flow feature finish feature_branch
            git flow release start 0.1.0
            git flow release finish '0.1.0'
            git flow hotfix start hotfix_branch
            git flow hotfix finish hotfix_branch
    
## forking workflow
    gives every developer their own forked server-side repository
    generally similar to gitflow with the dev's forked repo acting as develop repo
    generally the developers forked repo is called origin and the official repo is called upstream
    only proj lead/maintainer can authorise pull reqs
    fork repo -> locally clone -> git remote path for official repo addeded for local clone -> new local feature branch created -> branch pushed to forked repo -> open a pull request from the forks new branch to the official repo -> if approved the branch is merged in the official repo
    

rebasing
    process of mving/combining a seq of commits to a new base commit
        change a branches base to anouter commit, so its as if you branched the new commit (so your history is clean)
        use: master branch progressed past your feature branch
