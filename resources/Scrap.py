import random
from types import SimpleNamespace

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#Class Scrapper
class Scraper():
    def __init__(self):
        self.__api_keys__ = [os.getenv('API_KEY_2', 'demo'), os.getenv('API_KEY_3', 'demo')]
        self.__base_url__ = os.getenv('BASE_URL', 'https://www.alphavantage.co/query?')

    # returns an random api key from the list of api keys
    def __api_key__(self):
        return random.choice(self.__api_keys__)
    
    def winners_losers_actives(self):
        url = f"{self.__base_url__}function=TOP_GAINERS_LOSERS&apikey={self.__api_key__}" 
        r = requests.get(url)
        raw_data = r.json()
        data = SimpleNamespace(
            winners= raw_data.get('top_gainers', []),
            losers= raw_data.get('top_losers', []),
            actives= raw_data.get('most_actively_traded', [])
        ) if raw_data else SimpleNamespace(winners=[], losers=[], actives=[])
        return data
        
    def company_info(self, ticker):
        url = f"{self.__base_url__}function=OVERVIEW&symbol={ticker}&apikey={self.__api_key__}"
        r = requests.get(url)
        data = r.json()
        return SimpleNamespace(**data) if data else None

    def get_info_and_1D_graph(self, ticker):
        url = f"{self.__base_url__}function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey={self.__api_key__}"

    def get_1M_graph(self, ticker):
        url = f"{self.__base_url__}function=TIME_SERIES_MONTHLY&symbol={ticker}&apikey={self.__api_key__}"

    def get_1Y_graph(self, ticker):
        url = f"{self.__base_url__}function=TIME_SERIES_YEARLY&symbol={ticker}&apikey={self.__api_key__}"

   
if __name__ == "__main__":
    # Test
    scrap = Scraper()
    
    print("\n\n\n\n-------------------------------------\n", scrap.winners_lossers_actives().winners)
