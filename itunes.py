import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://music.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

object = response.json()
for result in object ["results"]:
    print(result["trackName"])