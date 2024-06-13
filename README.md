# Wake-On-LAN Service

This is a very simple python Wake-On-Lan Service that can be:
I use this to turn on devices using Home Assistant, as the integrated functionality led me dowwn this path instead.

# 1. Build
```
python -m venv venv
source bin/activate
pip install -r requirements.txt

docker-compose build
```

# 2. Run
```
#either use:
source bin/activate
python app.y

# or
docker-compose up -d
```

# 3. Used / Invoked
```
curl -vv -X POST -H "Content-Type: application/json" -d '{"macid": "a8:a1:59:5f:4c:c2"}' http://localhost:3090/wake_on_lan
```
