import requests
from datetime import datetime

urls = ["https://livescore-football.p.rapidapi.com/soccer/matches-by-league",
        "https://livescore-football.p.rapidapi.com/soccer/league-table"
        ]

querystring = [{"country_code": "england",
                "league_code": "premier-league", "timezone_utc": "0:00"},
               {"country_code": "england", "league_code": "premier-league"}]

headers = [{
    'x-rapidapi-key': "a211671f52msh0c9150df05ba8bbp167c03jsn6ab2a432ba9b",
    'x-rapidapi-host': "livescore-football.p.rapidapi.com"
}, {
    'x-rapidapi-key': "a211671f52msh0c9150df05ba8bbp167c03jsn6ab2a432ba9b",
    'x-rapidapi-host': "livescore-football.p.rapidapi.com"
}]

response = requests.request(
    "GET", urls[0], headers=headers[0], params=querystring[0]).json()

teamList = ['Tottenham Hotspur', 'Brighton & Hove Albion',
            'Manchester City', 'Southampton', 'Sheffield United',
            'Liverpool', 'Aston Villa', 'Crystal Palace', 'West Ham United',
            'Leicester City', 'Wolverhampton Wanderers', 'Newcastle United',
            'Manchester United', 'Burnley', 'Everton', 'Fulham',
            'West Bromwich Albion', 'Arsenal', 'Leeds United', 'Chelsea']

status = response['status']
# for complete team information
# data = response['data']['total']

# today and tomrow Games
# data1 = response['data']

# Get information Team
queryTeam = 'Manchester City'
# for team in data:
#     if team['team_name'] == 'Manchester City':
#         print(queryTeam)
#         print("-----------------------------------------")
#         print(f"Postion         : {team['rank']}")
#         print(f"Points          : {team['points']}")
#         print(f"Games Played    : {team['games_played']}")
#         print(f"Goal Difference : {team['goals_diff']}")
#         print(f"Wins            : {team['won']}")
#         print(f"Loses           : {team['lost']}")
#     break

# for game in data:
#     homeTeam = game['team_1']['name']
#     awayteam = game['team_1']['name']
#     teamName.add(homeTeam)
#     teamName.add(homeTeam)
# score = data['score']
# time = data['time']
# print(teamName)


# Get complete table Informaton
# print(f"{'#':>2}\t{'TEAM':<20}\t{'P':<2}\t{'GD':>3}\t{'PTS':<2}")
# print("------------------------------------------------------")
# for i, team in enumerate(data):
#     teamList.add(team['team_name'])
#     print(
#         f"{(i+1):>2}\t{team['team_name']:<20}\t{team['games_played']:<2}\t{team['goals_diff']:>3}\t{team['points']:<2}")
# print(teamList)

def getData(tDay=True):
    if tDay:
        response = requests.request(
            "GET", urls[0], headers=headers[0], params=querystring[0]).json()
        return response['data']
    return response['data']['total']


data1 = getData(tDay=True)

# Get todays matches
today = datetime.today().strftime("%Y%m%d")
today = '20210306'


for match in data1:
    startTime = str(match['time']['start'])[:8]
    if today == startTime:
        team1Name = match['team_2']['name']
        team2Name = match['team_1']['name']
        team1Score = match['score']['full_time']['team_1']
        team2Score = match['score']['full_time']['team_2']
        status = match['status']

        print(
            f"{team1Name:<22} {team1Score}    :   {team2Name:<22} {team2Score} {status}")
