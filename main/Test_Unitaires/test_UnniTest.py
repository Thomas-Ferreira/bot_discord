import unittest
from Data.Api import Api
import requests

def getResultApi(arg) :
    data = Api()
    dict = data.dataPybooru(arg)
    return dict

def getFreegames():
    url = "https://free-epic-games.p.rapidapi.com/free"

    headers = {
	    "X-RapidAPI-Key": "457bbd6e0amsh55fdc64aac40026p169136jsn5b55be2e29cd",
	    "X-RapidAPI-Host": "free-epic-games.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers)

    return res

class TestApiMethods(unittest.TestCase):

    def setUp(self):
        self.scrapper_1 = Api()
        self.test_dict = self.scrapper_1.dataPybooru('raiden_shogun')
    
    def test_data(self):
       self.assertIsInstance(self.test_dict, dict)

class TestBotMethods(unittest.TestCase):

    dict1 = {"id": 1, "url": 'url'}
    dict2 = {}
    
    def test_getResultApiTrue(self):
        getResultApi(self.dict1)

class TestEpicGamesMethods(unittest.TestCase):
    
    def test_freeGames(self):
        self.assertEqual(getFreegames().status_code, 200)


if __name__ == '__main__':
    unittest.main()
