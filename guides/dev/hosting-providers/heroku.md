#shell
##Heroku workflow
    Create git local repo -> Login to heroku -> create heroku-app -> add assets -> deploy app (push to heroku git)

##Login to heroku
    heroku login
    //enter email and password

##Create app and heroku git remote repositary (associated with the local one)
    heroku create weather-app-em-2018

##Add assets
    heroku addons:create heroku-postgresql:hobby-dev --name=weather-db

##Deploy the app
    //add all needed files to the local repo and commit them
    //Then push to heroku-git-remote-repositary
        git push heroku master
    //Make sure one instance of the app is running
        heroku ps:scale web=1
    //Visit generated url
        heroku open

##Test locally
    heroku local

##maintain app
    //Remove connected heroku-git-remote-repositary from local and remote origin repo's
        git remote rm -a git remote rm https://git.heroku.com/guarded-fjord-34473.git
    //Check remote repo's
        git remote -v
    //Change the connected heroku-git-remote-repositary
        heroku git:remote -a weather-app-em-2018
