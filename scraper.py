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

        if home["team"]["name"] == team:
            oldscore = currentscore
            currentscore = home["score"][0]["score"] #CURRENT SCORE IS CHANGED HERE
            if currentscore != oldscore:
                print("currentscore: " + str(currentscore) + " old score:" + str(oldscore))
                print("{} {} - {} {}".format(home["team"]["name"], home["score"][0]["score"], away["score"][0]["score"], away["team"]["name"]))  
                continue
        elif away["team"]["name"] == team:
            oldscore = currentscore
            currentscore = away["score"][0]["score"] #CURRENT SCORE IS CHANGED HERE
            if currentscore != oldscore:
                print("currentscore: " + str(currentscore) + " old score:" + str(oldscore))
                print("{} {} - {} {}".format(home["team"]["name"], home["score"][0]["score"], away["score"][0]["score"], away["team"]["name"]))  
                continue
    return currentscore

currentscore=0
while True:
    currentscore=ScrapeScore(currentscore, "Arsenal")
    resp = sms.sendSMS('0NSUV4UG8RI-YvAmaTvH17jQLhwcQRPq7JnTlmz7IO', '353858158414, 353852704841',
        'Pornhub', 'Chuckles?')
    time.sleep(5)