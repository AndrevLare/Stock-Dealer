import random
from types import SimpleNamespace

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#Class Scrapper
class Scraper():
    """Scraper class to interact with the Alpha Vantage API."""
    def __init__(self):
        self.__api_keys__ = [os.getenv('API_KEY_2', 'demo'), os.getenv('API_KEY_3', 'demo'), os.getenv('API_KEY_4', 'demo'), 
                             os.getenv('API_KEY_5', 'demo'), os.getenv('API_KEY_6', 'demo'), os.getenv('API_KEY_7', 'demo'), 
                             os.getenv('API_KEY_8', 'demo'), os.getenv('API_KEY_9', 'demo'), os.getenv('API_KEY_10', 'demo'),
                             os.getenv('API_KEY_11', 'demo'), os.getenv('API_KEY_12', 'demo'), os.getenv('API_KEY_13', 'demo')]
        self.__base_url__ = os.getenv('BASE_URL', 'https://www.alphavantage.co/query?')

    # returns an random api key from the list of api keys
    def __api_key__(self):
        """Get a random API key from the list of available keys."""
        return random.choice(self.__api_keys__)
    
    def winners_losers_actives(self):
        """Get top gainers, losers, and most actively traded stocks."""
        
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
        """Get company information for a given ticker."""
        
        url = f"{self.__base_url__}function=OVERVIEW&symbol={ticker}&apikey={self.__api_key__}"
        r = requests.get(url)
        data = r.json()
        return SimpleNamespace(**data) if data else None

    def get_info_and_1D_graph(self, ticker):
        """Get company information and 1-day graph data for a given ticker."""
        
        url = f"{self.__base_url__}function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=15min&apikey={self.__api_key__}"
        r = requests.get(url)
        raw_data = r.json()
        first_timestamp = list(raw_data["Time Series (15min)"].keys())[0]
        values = []
        for i, e in enumerate(raw_data["Time Series (15min)"]):
            if i > 95:  # Limit to the last 30 days
                break
            values.append(raw_data["Time Series (15min)"][e].get('4. close', 0))
            
        data = SimpleNamespace(
            last_refreshed=raw_data.get('Meta Data', {}).get('3. Last Refreshed', ''),
            current_value = raw_data["Time Series (15min)"][first_timestamp].get('1. open', 'Open Vacio'),
            values = values,
        )
        return data if raw_data else None

    def get_1M_graph(self, ticker):
        """Get 1-month graph data for a given ticker."""
        
        url = f"{self.__base_url__}function=TIME_SERIES_DAILY&symbol={ticker}&apikey={self.__api_key__}"
        r = requests.get(url)
        raw_data = r.json()
        values = []
        for i, e in enumerate(raw_data["Time Series (Daily)"]):
            if i > 30:  # Limit to the last 30 days
                break
            values.append(raw_data["Time Series (Daily)"][e].get('4. close', 0))
            
        data = SimpleNamespace(
            last_refreshed=raw_data.get('Meta Data', {}).get('3. Last Refreshed', ''),
            values = values,
        )
        return data if raw_data else None

    def get_1Y_graph(self, ticker):
        """Get 1-year graph data for a given ticker."""
        
        url = f"{self.__base_url__}function=TIME_SERIES_WEEKLY&symbol={ticker}&apikey={self.__api_key__}"
        r = requests.get(url)
        raw_data = r.json()
        values = []
        for i, e in enumerate(raw_data["Weekly Time Series"]):
            if i > 48:  # Limit to the last 48 weeks (1 year)
                break
            values.append(raw_data["Weekly Time Series"][e].get('4. close', 0))
            
        data = SimpleNamespace(
            last_refreshed=raw_data.get('Meta Data', {}).get('3. Last Refreshed', ''),
            values = values,
        )
        return data if raw_data else None

   
if __name__ == "__main__":
    # Test
    scrap = Scraper()
    print(scrap.get_info_and_1D_graph('AAPL'))
    print("Estas en un entorno de pruebas para Scrapper, si quieres ejecutar el programa, ejecuta el main.py")