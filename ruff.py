import requests
import json

url = "https://studystreak.in/api/login/"

payload = json.dumps({
  "username": "admin",
  "password": "admin"
})
headers = {
  'Content-Type': 'application/json',
}
for _ in range(50):
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
