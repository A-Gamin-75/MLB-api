import requests
from datetime import date
import sys
import statsapi
from pprint import pprint
import json
import os
from pprint import pprint
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/Documents/jupyter/MLB/credentials/mlb-analysis-463501-869e729270f3.json")


guardiansStats = []
gamePk = 777429
teamId = 114

getRosterUrl = f"https://statsapi.mlb.com/api/v1/teams/{teamId}/roster?rosterType=25Man"
roster = requests.get(getRosterUrl)
roster = roster.json()
roster_list = roster.get("roster",[])

guardsStatsLife = []
gamePk = 777411
for player in roster_list:
    person = player['person']
    player_id = person['id']
    #jersey = person['jerseyNumber']
    player_name = person['fullName']
    status = player['status']
    getStatsUrl = f"https://statsapi.mlb.com/api/v1/people/{player_id}/stats?type=career"
    playerStats = requests.get(getStatsUrl)
    playerStats = playerStats.json()
    print(f"Player ID: {player_id}, Name: {player_name}, Status: {status['description']}\n")
    #print(f"Stats (lifetime): {playerStats['stats']['splits']}")
    pprint(playerStats)
    sys.exit()
    guardsStatsLife.append(playerStats)

# client = bigquery.Client()
# print("Project:", client.project)

sys.exit()

