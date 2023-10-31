import requests

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

def getAllBooks():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    print(getAllBooks())