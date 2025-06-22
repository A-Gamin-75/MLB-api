import requests
from datetime import date
import sys
import statsapi
from pprint import pprint
import json
import os
from google.cloud import bigquery

# os.chdir(os.path.expanduser("~\Documents\jupyter\MLB"))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/Documents/jupyter/MLB/credentials/mlb-analysis-463501-869e729270f3.json")

# List of official MLB team IDs
mlb_team_ids = [
    108, 109, 110, 111, 112, 113, 114, 115,
    116, 117, 118, 119, 120, 121, 133, 134,
    135, 136, 137, 138, 139, 140, 141, 142,
    143, 144, 145, 146, 147, 158
]

guardiansStats = []
gamePk = 777429
teamId = 114

getRosterUrl = f"https://statsapi.mlb.com/api/v1/teams/{teamId}/roster"
roster = requests.get(getRosterUrl)
roster = roster.json()
roster_list = roster.get("roster",[])


for player in roster_list:
    print(keys(player))
    person = player['person']
    # person = player.get('person',{})
    player_id = person['id']
    player_name = person['fullName']
    status = player['status']

    print(f"Player ID: {player_id}, Name: {player_name}, Status: {status}")


client = bigquery.Client()
print("Project:", client.project)

sys.exit()

