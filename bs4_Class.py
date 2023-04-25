import datetime
from bs4 import BeautifulSoup
import requests
from statistics import mean


class FindData:
    def __init__(self, location):
        self.prices_page1 = None
        self.response_pageX = None
        self.over_2000_perc = None
        self.between_perc = None
        self.bellow_900_perc = None
        self.sampling_size = None
        self.min = None
        self.max = None
        self.average = None
        self.location = location
        self.response = None
        self.page = None
        self.prices = None
        self.data = None

    def find_prices(self, url, tag, selector):
        self.response = requests.get(url)
        self.page = BeautifulSoup(self.response.text, 'html.parser')
        self.data = self.page.find_all(tag, class_=selector)
        self.prices = [int(price.getText().strip().replace(' ', '').split('€')[0]) for price in self.data if price.getText().strip().replace(' ', '') != 'Preçosobconsulta' and
                       int(price.getText().strip().replace(' ', '').split('€')[0]) < 5000]

        return sorted(self.prices)

    def stats(self, prices):
        print(self.location, f'on {datetime.datetime.now()}')
        print(sorted(prices))
        self.average = mean(prices)
        print('Average price: ', round(self.average), '€')
        self.max = max(prices)
        self.min = min(prices)
        self.sampling_size = len(prices)
        count = 0
        count2 = 0
        count3 = 0
        for price in prices:
            if price < 900:
                count += 1
            if 900 < price < 2000:
                count2 += 1
            if price > 2000:
                count3 += 1

        self.bellow_900_perc = round((count / self.sampling_size) * 100)
        self.between_perc = round((count2 / self.sampling_size) * 100)
        self.over_2000_perc = round((count3 / self.sampling_size) * 100)
        print('Max price = ', self.max, '€')
        print('Min price = ', self.min, '€')
        print(self.bellow_900_perc, '% :listed houses under 900€')
        print(self.between_perc, '% :listed houses between 900€ and 2000€')
        print(self.over_2000_perc, '% :listed houses over 2000€')
        print('Sampling data size: ', self.sampling_size)
        print('--------------END-----------------')
        data_dict = {
            "location": self.location,
            "data": sorted(prices),
            "average": round(self.average),
            "max_price": self.max,
            "min_price": self.min,
            "under_900eur": round(self.bellow_900_perc),
            "between_900_2000eur": round(self.between_perc),
            "over_2000eur": round(self.over_2000_perc),
            "sampling_size": self.sampling_size
        }
        return data_dict
