
import requests
from datetime import datetime

urls = ["https://api-nba-v1.p.rapidapi.com/games/live/",
        "https://api-nba-v1.p.rapidapi.com/games/league/standard/2020"]

headers = {
    'x-rapidapi-key': "a211671f52msh0c9150df05ba8bbp167c03jsn6ab2a432ba9b",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
}

response = requests.request("GET", urls[1], headers=headers).json()

if int((response['api']['status']) == 200):
    print('okay')
    games = response['api']['games']
    for g in games:
        print(g['startTimeUTC'])
