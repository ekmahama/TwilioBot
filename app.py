import requests
import os
from flask import Flask, request
from dateutil import tz
from twilio.twiml.messaging_response import MessagingResponse


# API endpoint information

urls = ["https://livescore-football.p.rapidapi.com/soccer/matches-by-league",
        "https://livescore-football.p.rapidapi.com/soccer/league-table"
        ]

querystring = [{"country_code": "england",
                "league_code": "premier-league", "timezone_utc": "0:00"},
               {"country_code": "england", "league_code": "premier-league"}]


# Team List
teamList = ['Tottenham Hotspur', 'Brighton & Hove Albion',
            'Manchester City', 'Southampton', 'Sheffield United',
            'Liverpool', 'Aston Villa', 'Crystal Palace', 'West Ham United',
            'Leicester City', 'Wolverhampton Wanderers', 'Newcastle United',
            'Manchester United', 'Burnley', 'Everton', 'Fulham',
            'West Bromwich Albion', 'Arsenal', 'Leeds United', 'Chelsea']


to_zone = tz.gettz('America/New_York')

app = Flask(__name__)


def getData(tDay=True):
    if tDay:
        response = requests.request(
            "GET", urls[0], headers=headers[0], params=querystring[0]).json()
        return response['data']
    return response['data']['total']


def getTeamList(output, queryTeam, data):
    for team in data:
        if team['team_name'] == queryTeam:
            output += f"{queryTeam}\n"
            output += f"{'-----------------------------------------'}\n"
            output += f"Postion         : {team['rank']}\n"
            output += f"Points          : {team['points']}\n"
            output += f"Games Played    : {team['games_played']}\n"
            output += f"Goal Difference : {team['goals_diff']}\n"
            output += f"Wins            : {team['won']}\n"
            output += f"Loses           : {team['lost']}\n"
        break
    return output


def getLeagueTable(output, data):
    output += f"{'#':>2}\t{'TEAM':<20}\t{'P':<2}\t{'GD':>3}\t{'PTS':<2}\n"
    output = + \
        f"{'------------------------------------------------------'}\n"
    for i, team in enumerate(data):
        teamList.add(team['team_name'])
        output += f"{(i+1):>2}\t{team['team_name']:<20}\t{team['games_played']:<2}\t{team['goals_diff']:>3}\t{team['points']:<2}\n"
    return output


def gamesForToday(output, data1, toDay):
    for match in data1:
        startTime = str(match['time']['start'])[:8]
        if toDay == startTime:
            team1Name = match['team_2']['name']
            team2Name = match['team_1']['name']
            team1Score = match['score']['full_time']['team_1']
            team2Score = match['score']['full_time']['team_2']
            status = match['status']

            output += f"\n{team1Name:<22} {team1Score}    :   {team2Name:<22} {team2Score} {status}"

        if not output:
            output += "No matches happening today"

    return output


@app.route('/', method=['POST'])
def receive_sms():
    body = request.values.get('body', '').lower().strip()
    resp = MessagingResponse()

    output = ""
    if body == 'today':
        data1 = getData(tDay=True)
        toDay = datetime.today().strftime("%Y%m%d")

        output = gamesForToday(output, data1, toDay)

    elif body.lower() in teamList:
        data = getData(tDay=False)
        # Get information Team
        queryTeam = body.lower()

        output = getTeamList(output, queryTeam, data)

    elif body.lower() == 'table':
        data = getData(tDay=False)
        output = getLeagueTable(output, data)

    elif body.lower = "list":
        output = '\n'.join(teamList)

    else:
        output += f{'Sorry Not information available now'}

    resp.message(output)
    return resp


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run()
