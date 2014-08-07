import simplejson as json 
import requests
import http.client, urllib.parse
url = "api.weibo.com"
conn = http.client.HTTPSConnection(url);

params = urllib.parse.urlencode({'access_token': '2.00fzZntBEfJvWC4d9148e1b8XiP4KB'})
conn.request("GET", "/2/statuses/public_timeline.json", params, {})
res = conn.getresponse()

print (res)