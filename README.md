# api-driven-pi-buzzer

# Docker Multi Environment Seutp
```
docker buildx create --name mybuilder
docker buildx use mybuilder
docker buildx inspect --bootstrap
```

# Docker Build
docker buildx build --platform linux/amd64,linux/arm64,linux/386,linux/arm/v7,linux/arm/v6 -t elongstreet88/api-driven-pi-buzzer --push .

# Docker Run
```
docker run --device /dev/gpiomem -p 5000:5000/tcp elongstreet88/api-driven-pi-buzzer^C
```