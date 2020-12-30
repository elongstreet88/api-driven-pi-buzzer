# Overview
Simple web based API driven buzzer/led for a RasberryPI.
Only tested on version 4.
Uses flask and the GPIO library.

- Buzzer is expected to be on pin 17

To execute from docker on a PI, use:
```
docker run --device /dev/gpiomem -p 5000:5000/tcp elongstreet88/api-driven-pi-buzzer
```

# Docker Multi Environment Seutp
```
docker buildx create --name mybuilder
docker buildx use mybuilder
docker buildx inspect --bootstrap
```

# Docker Build
./build.sh

# Docker Run
```
./run.sh
```