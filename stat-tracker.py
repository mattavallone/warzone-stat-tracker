import http.client
import json
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('API_KEY')
HOST = os.getenv('API_HOST')
GAMERTAG = os.getenv('GAMERTAG')
PLATFORM = os.getenv('PLATFORM')

headers = {
    'X-RapidAPI-Key': KEY,
    'X-RapidAPI-Host': HOST
    }

conn = http.client.HTTPSConnection("call-of-duty-modern-warfare.p.rapidapi.com")

conn.request("GET", "/warzone-matches/" + GAMERTAG + "/" + PLATFORM, headers=headers)

res = conn.getresponse().read()
json_data = json.loads(res.decode("utf-8"))

# json_data = json.load(open("sample_response.json"))

try:
    for match in json_data['matches']:
    	print(match['playerStats']['teamPlacement'])
except:
    print("Error parsing response")