import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

fileName = "cso.json"


response = requests.get(url)

with open(fileName, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)