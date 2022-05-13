import unittest
from Data.Api import Api

class TestApiMethods(unittest.TestCase):

    def setUp(self):
        self.scrapper_1 = Api()
        self.test_dict = self.scrapper_1.dataPybooru('raiden_shogun')
    
    def test_data(self):
       self.assertIsInstance(self.test_dict, dict)

class TestBotMethods(unittest.TestCase):

    dict1 = {"id": 1, "url": 'url'}
    dict2 = {}
    
    def tes_getResultApiTrue(self):
        getResultApi(self.dict1)


def getResultApi(arg) :
    data = Api()
    dict = data.dataPybooru(arg)
    return dict

if __name__ == '__main__':
    unittest.main()
