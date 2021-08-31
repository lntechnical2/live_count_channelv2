# myvcbot


## HOW TO GET MESSAGE_ID 

```pip install requests```

```python
import requests  as re 
import json
chat_id = "" #chat_id with @  ex{@lntechnical}

token = "" #Bot token

text = 'Telegram Channel Live Subscriber Counting .... 🎉🎉\n\n pls wait for live count'

send_api = f"https://api.telegram.org/bot{token}/sendMessage"
data = {"chat_id":chat_id,
              "text" : text
}

res =re.post(send_api,data).content
value= json.loads(res)
try:
	result = value["result"]
except:
	print(res)
print(result["message_id"])
```
