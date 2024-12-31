
 docker-compose up -d

docker cp d:/docker/homeassistant/config homeassistant:/config


curl -X POST \
  -H "Authorization: Bearer YOUR_LONG_LIVED_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}' \
  http://your-home-assistant-ip:8123/api/services/script/turn_on_living_room_light



Long Lived Access Token generate from here

http://localhost:8123/profile/security

  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmOWI1ODJiNmU2ZWE0NTE0ODllYTM3ODNkM2Y4MjBiZCIsImlhdCI6MTczNDgxOTE1OSwiZXhwIjoyMDUwMTc5MTU5fQ.YiUBTj8e1BJEFAddfU1QG0eiY6kavd-dhwF3wP9UW64


https://python-kasa.readthedocs.io/en/latest/index.html

pip install python-kasa