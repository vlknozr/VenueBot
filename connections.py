import json
import requests
host = 'http://127.0.0.1:8000/'


url = host+"api/post/getVenuesAround/"

data = json.dumps({"neighborhood": "40700", "cuisine": [1,2,3], "price": "9", "rating": "1" })

response = requests.post(url, data=data)

if response.status_code == 200:
    print(response.text)
else:
    print(response)



