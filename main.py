import requests

#  for the past 30 days
url = 'https://api.frankfurter.app/2026-04-28..2026-05-28?from=USD'

response = requests.get(url)
data = response.json()

print(data)

class CurrencyDataPoint:
    def __init__(self, date, rate):
        self.date = date
        self.rate = rate

class CurrencyAnalyzer:
    def __init__(self):
        self.datapoints = []

    def load_data(self, raw_json, target_currency):
        for outerKey, innerKeys in raw_json['rates'].items():
            for currency in innerKeys.keys():
                if currency == target_currency:
                    self.datapoints.append(CurrencyDataPoint(outerKey, currency.value()))

    def calculate_mean(self):
        pass