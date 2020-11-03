import requests
import json
import time
import sms
from bs4 import BeautifulSoup as bs

def ScrapeScore(currentscore, team):
    response = requests.get('https://www.sportinglife.com/football/live')

    json_data=bs(response.content,"html.parser").find("script",id="__NEXT_DATA__").string

    matches=json.loads(json_data)["props"]["pageProps"]["matches"]
    for match in matches:
        home= match["team_score_a"]
        away= match["team_score_b"]
        if home["team"]["name"] == team or away["team"]["name"] == team:
            oldscore = currentscore
            currentscore = int(home["score"][0]["score"]) + int(away["score"][0]["score"])
            if currentscore != oldscore:
                print("currentscore: " + str(currentscore) + " old score:" + str(oldscore))
                notification = "({}) {} [{}] - {} [{}] ".format(match["clock"], home["team"]["name"], home["score"][0]["score"], away["team"]["name"], away["score"][0]["score"])
                print(notification) 
                sms.sendSMS('5IDrV18jaeo-dalDi7VyEEoVaDtQjvW5GBb46kA3DP', '353858158414, 353852704841', 'GoalSend', notification)
                continue
    return currentscore

currentscore=0
oldscore=0
while True:
    currentscore=ScrapeScore(currentscore, "Liverpool")
    time.sleep(5)