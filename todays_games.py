import requests
from datetime import date

# # Get today's schedule
today = date.today().isoformat() 
print(date.today())
url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={today}"

resp = requests.get(url)
schedule = resp.json()

# Grab all gamePks for today
games = schedule['dates'][0]['games']
for game in games:
    print(f"{game['teams']['away']['team']['name']} ({game['teams']['away']['team']['id']}) at {game['teams']['home']['team']['name']} ({game['teams']['home']['team']['id']})")
    print(f"gamePk: {game['gamePk']}")
    
