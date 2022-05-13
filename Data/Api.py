from turtle import pos
import requests
from pprint import pprint
import json
from pybooru import Moebooru

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
    
    def dataPybooru(self, tag) :
        client = Moebooru('konachan')
        li_url = []
        li_rating = []
        posts = client.post_list(tags =tag, limit = 100)

        for post in posts:
            url =  post['file_url']
            rating = post['rating']
            if rating == 'e':
                li_url.append('|| {0} ||'.format(url))
            else :
                li_url.append(url)
                li_rating.append(rating)

        dictionary = {i : li_url[i] for i in range(0, len(li_url) ) }

        return dictionary
