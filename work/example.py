import simplejson as json 
import requests
url = "https://api.weibo.com/2/friendships/friends.json"
payload = {"profile": { "userid": "1234567890", "network":"twitter" } }
headers = {"Content-Type": "application/json"}
r = requests.post(url, data=json.dumps(payload),headers=headers)
r.json()