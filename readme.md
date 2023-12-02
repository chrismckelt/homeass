docker cp config/. container_id:/target


docker run --restart always -d --name homeassistant -v d:/docker/homeassistant/config:/config -e TZ=Australia/Perth --net=host ghcr.io/home-assistant/home-assistant:stable

