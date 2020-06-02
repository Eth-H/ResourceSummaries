# git setup
	//Create repositary at Github.com
	//Convert local react project to a git repositary
		git init
		//Add the created repositary as a remote repositarty
			git remote add origin https://github.com/Eth-H/JPP
		echo node_modules > .gitignore	
		git add .
		git commit -m "initial commit"
		git push origin master -f
		// If getting consistant errors can pull the repositary
			git pull  https://github.com/Eth-H/JPP master --allow-unrelated-histories	

# Setup file system and dependancies
    //Create parent directory
    //Create server child directory  (the client sub-direcotry is created by create-react app)

## setup client side (react)
    npm install create-react-app -g
	//Create app specify name, can specify path
		npx create-react-app my-app
	//Go to directory with app
		cd my-app

## Seting up the server
    npm init
    npm install body-parser cookie-parser express request request-promise --save
    npm install concurrently nodemon --save-dev
### package.json
	//server
		"scripts": {
			"test": "echo \"Error: no test specified\" && exit 1",
			"client": "npm start --prefix client",
			"start": "node server",
		},
		//if using concurrently nodemon dev packages, add to scripts 
			"server": "nodemon server",
			"dev": "concurrently \"npm run server\" \"npm run client\"",
		//if using heroku, add to scripts
			"heroku-postbuild": "cd client && npm install && npm run build"
		

		 //Setup for deployment to github pages (independant deployment)
			//then add a homepage field to package.json (url thet the app lives on):
				"homepage": "https://user.github.io/proj/",
			//deployment setup
				//then add scripts for target
					"scripts": {
						"predeploy": "npm run build",
						"deploy": "gh-pages -d build"
					}
				//Add dependancies for deployment method/target  EG github pages
					npm install --save-dev gh-pages
				//Run build
					npm run build
				//Deploy to target EG github pages  (Carry out git setup before this command)
					npm run deploy	
### setup database
	//postgres
	//Use pgAdmin or CLI to create local database
	//Fill that local db using SQL queries (with the Query Tool)
	//Add postgres to path (on windows)
		C:\Program Files\PostgreSQL\10\bin
	npm install pg --save


# deploy
	//Start development server
		npm start
    //run server
		node src/server/index.js

# useful packages
## backend
    body-parser, cookie-parser, hash.js, uuid
    //dev
        concurrently, nodemon
    //http
        request request-promise
    //server
        express        
    //sql drivers
        pg    
## client
    //date, time
        date-arithmetic: 3.1.0
        //localizer
            moment
        react-big-calendar
        react-day-picker
    event-stream
    react-bootstrap
    //routing
        react-router
        react-router-bootstrap
        react-router-dom


# testing with jest
    //setup
        //Optionally install typescript definitions
            //npm i @types/jest
        npm install --save-dev jest jest-fetch-mock enzyme enzyme-adapter-react-16
        //Run test, can optionally pass directory 
            npm test --file_name/path



//Using webtest.io (don't install in project folder (webpackage update problem))
    //Install it client for it
        npm install wt-cli
    //Initilize wt
        wt init
    //Create first webhook, this will make a file and a browser
        echo "module.exports = function (cb) {cb(null, 'Hello');}" > hello.js
        wt create hello.js
    //Open webhook in browser application
        wt edit hello
    //Update file (if you edit it locally)
