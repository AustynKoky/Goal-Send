import requests
import json
import time
from bs4 import BeautifulSoup as bs

team = "Boavista"
currentscore = 0

def ScrapeScore():
    response = requests.get('https://www.sportinglife.com/football/live')

    json_data=bs(response.content,"html.parser").find("script",id="__NEXT_DATA__").string

    matches=json.loads(json_data)["props"]["pageProps"]["matches"]
    for match in matches:
        home= match["team_score_a"]
        away= match["team_score_b"]

        if home["team"]["name"] == team:
            global currentscore
            oldscore = currentscore
            currentscore = home["score"][0]["score"] #CURRENT SCORE IS CHANGED HERE
            if currentscore != oldscore:
                print("currentscore: " + str(currentscore) + " old score:" + str(oldscore))
                print("{} {} - {} {}".format(home["team"]["name"], home["score"][0]["score"], away["score"][0]["score"], away["team"]["name"]))
        

    time.sleep(30)
    ScrapeScore()
    
ScrapeScore()