//Start daemon
    service docker start
# setup
    //login to dockerhub
        docker login --username $dockerId

# docker image
    immutable image that will act as the fs of a docker container
## manually create
    create a dockerfile, this will describe how to make an image
    //EG
        # start from this image
        FROM node:current-slim
        # set cwd
        WORKDIR /usr/src/app
        # Copy the file from your host to dockers cwd
        COPY package.json .
        # run cmd inside img fs
        RUN npm install
        # Inform Docker that the container is listening on the specified port at runtime
        EXPOSE 8080
        # Run the specified command within the container
        CMD [ "npm", "start" ]
        # copy remaining sourcecode
        COPY ...
    // build from dockerfile
        //-t/--tag
        docker build -t idk -t $dockerId/proj:1.0 .
        docker build -t $dockerId/proj:1.0 -f /path/to/a/Dockerfile .
        docker build -t $dockerId/proj:1.0 -t shykes/myapp:latest .
    //add tags later using original tag
        docker image tag idk $dockerId/proj:1.0
    // push to dockerhub
        docker image push $dockerId/proj:1.0

    // run container
        //-p/--publish: forward host 8000 to container 8080
        //-d/--detach: run in bg, --name: referable name
        docker run --publish 8000:8080 --detach --name bb bulletinboard:1.0
    // rm a container
        docker rm --force bb

## fetch a base image
    //https://hub.docker.com/
    docker pull kalilinux/kali-linux-docker


// get images history
    docker image history helloworld

//Run program inside container
    docker run -i -t kalilinux/kali-linux-docker [programName]		
//images: see avaliable images and get details (EG containerID), ps: List running containers	
//commit [containerID] [imageName]:	Save current state as image
//rmi [imageName]: remove image
    docker {}
//stop [containerID]: Stop container, rm [containerID]: del files created on host node by that server
    docker {} 

# run apps on docker instance
    //Mount external host system 
        docker run -it -v /temp/:/home/ kalilinux/kali-linux-docker /bin/bash
    //Attach docker port to external system port
        docker run -it -v /temp/:/home/ -p 4567:80 kalilinux/kali-linux-docker /bin/bash
    //Mount x server file
        docker run -it -v -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \ kalilinux/kali-linux-docker /bin/bash
//Move image
    //push [imageName]: Push it on the docker online repo, export [imageName]: export as archive
        docker {} 				

# links
    https://docs.docker.com/get-started/part2/#clonewin
    https://championshuttler.github.io/docker-basicLearning/#setting-up-your-machine
    https://training.play-with-docker.com/
    https://github.com/kelseyhightower/kubernetes-the-hard-way
    https://linuxacademy.com/course/kubernetes-the-hard-way/
    https://github.com/etadata/owasp-workshop
    https://stackoverflow.com/questions/47536536/whats-the-difference-between-docker-compose-and-kubernetes
    https://docker-curriculum.com/
