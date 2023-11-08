import requests
import datetime
import json
URL="http://127.0.0.1:8000/api/history"

data={
    'Desciption_change':'a lot of things has been changed',
    'time':datetime.datetime.now().isoformat(),
    'task':'jklnlsdalj',
    'user':'shirjeel',
}
jason_data=json.dumps(data)
r=requests.post(url=URL,data=jason_data)
# data=r.json()
print(data)