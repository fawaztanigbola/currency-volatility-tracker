import requests

#  for the past 30 days
url = 'https://api.frankfurter.app/2026-04-28..2026-05-28?from=USD'

response = requests.get(url)
data = response.json()

# print(data['rates'])

# obj = []

class CurrencyDataPoint:
    def __init__(self, date, rate):
        self.date = date
        self.rate = rate

    def __str__(self):
        return '{} {}'.format(self.date, self.rate)
    
    def __repr__(self):
        return '{} {}'.format(self.date, self.rate)

class CurrencyAnalyzer:
    def __init__(self):
        self.datapoints = []

    def load_data(self, raw_json, target_currency):
        for rate_date, rate in raw_json['rates'].items():
            self.datapoints.append(CurrencyDataPoint(rate_date, rate[target_currency]))

    def calculate_mean(self):
        for datapoint in self.datapoints:
            return datapoint

    def calculate_variance(self):
        pass

    def calculate_volatility(self):
        pass

eur_analysis = CurrencyAnalyzer()

eur_analysis.load_data(data, 'ZAR')

print(eur_analysis.datapoints)



# print(obj)