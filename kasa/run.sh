docker cp d:/docker/homeassistant/config homeassistant:/config

docker cp homeassistant:/tmp c:/dev/homeassistant/kasa

docker cp c:/dev/homeassistant/kasa/tmp/python-kasa/pyproject.toml homeassistant:/tmp/python-kasa/pyproject.toml

docker exec -it homeassistant bash