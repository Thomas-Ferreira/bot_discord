import unittest
from Data.Api import Api
import App

class TestApiMethods(unittest.TestCase):

    def setUp(self):
        self.scrapper_1 = Api()
        self.test_dict = self.scrapper_1.dataPybooru('raiden_shogun')
    
    def test_data(self):
       self.assertIsInstance(self.test_dict, dict)

class TestBotMethods(unittest.TestCase):

    def setUp(self):
        self.scrapper_1 = Api()
        self.test_dict = self.scrapper_1.dataPybooru('raiden_shogun')


if __name__ == '__main__':
    unittest.main()
