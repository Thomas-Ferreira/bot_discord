from ast import If
import requests
from pprint import pprint
import json

class EpicGamesApi :

    url = "https://free-epic-games.p.rapidapi.com/free"

    headers = {
	    "X-RapidAPI-Key": "457bbd6e0amsh55fdc64aac40026p169136jsn5b55be2e29cd",
	    "X-RapidAPI-Host": "free-epic-games.p.rapidapi.com"
        }
    
    def __init__(self) :

        self.res = requests.request("GET", self.url, headers=self.headers)
        li_url = []
        json_item = json.loads(self.res.text)

        for item in range(0,100):
            url =  json_item[item]['file_url']
            li_url.append(url)
    
        self.dictionary = {i : li_url[i] for i in range(0, len(li_url) ) }
    
    def getFreeGames (self) :
        
        return self.dictionary
