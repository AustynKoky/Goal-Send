import requests
import json
from bs4 import BeautifulSoup as bs

response = requests.get('https://www.sportinglife.com/football/live')

json_data=bs(response.content,"html.parser").find("script",id="__NEXT_DATA__").string

matches=json.loads(json_data)["props"]["pageProps"]["matches"]
for match in matches:
    home= match["team_score_a"]
    away= match["team_score_b"]
    print("{} {} - {} {}".format(home["team"]["name"], home["score"][0]["score"], away["score"][0]["score"], away["team"]["name"]))