import pandas as pd
import requests
from pprint import pprint
import json

class Api :

    def data(self) :

        res=requests.get('https://yande.re/post.json?limit=100&tags=genshin_impact')
        li_url = []
        json_item = json.loads(res.text)

        for item in range(0,100):
            url =  json_item[item]['file_url']
            li_url.append(url)
    
        dictionary = {i : li_url[i] for i in range(0, len(li_url) ) }

        return dictionary

#data = Api()
#dict = data.data()
#pprint(dict[0])
