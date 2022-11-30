import requests
import keys

key = keys.STEAM_KEY
LEAGUE_ID = 14506

url = f"https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/?key={key}&league_id={LEAGUE_ID}"

print(url)