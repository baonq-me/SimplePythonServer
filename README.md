# SimplePythonServer

This is how I do this project

## Clone this project 

```
git clone https://github.com/baonq-me/SimplePythonServer
```

## Build 

```
cd SimplePythonServer
docker build -t quocbao747/simplepythonserver:1.0 .
```

## RUN

Expose port `8080` from container to port `9090` in host machine

```
docker run -d -p 9090:8080 quocbao747/simplepythonserver:1.0
```

## Test

```
➜  ~ curl localhost:9090
Hello, world
➜  ~
```

## Push to Docker Hub
  
```
docker login # only need to do once
docker push quocbao747/simplepythonserver:1.0 
```

## Do your own

Do your own project then start from `Build` by following the naming convention of images when pushing to Docker hub as `<hub-user>/<repo-name>:<tag>`
