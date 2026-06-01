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
        return str(self.rate)
    
    def __repr__(self):
        return str(self.rate)

class CurrencyAnalyzer:

    def __init__(self):
        self.datapoints = []
    
    def get_total_days(self):
        return len(self.datapoints)

    def load_data(self, raw_json, target_currency):
        for rate_date, rate in raw_json['rates'].items():
            self.datapoints.append(CurrencyDataPoint(rate_date, rate[target_currency]))

    def calculate_mean(self):
        if not self.datapoints:
            return 0.0
        
        rate_sum = 0.0
        for datapoint in self.datapoints:
            rate_sum += datapoint.rate

        return rate_sum / self.get_total_days()

    def calculate_variance(self):
        total_date = self.get_total_days()
        if total_date == 0:
            return 0.0
        variance_sum = 0.0
        mean = self.calculate_mean()
        for datapoint in self.datapoints:            
            variance_sum += (datapoint.rate - mean)**2

        return variance_sum / total_date
        

    def calculate_volatility(self):
        return self.calculate_variance() ** 0.5

# Prompt user 
target_currency = input('Input Currency Code: ')

analysis = CurrencyAnalyzer()

analysis.load_data(data, target_currency)

print('--- Analysis Of {} Currency ---'.format(target_currency))
print('Total days analyzed: {}'.format(analysis.get_total_days()))
print('Average rate: {:.4f}'.format(analysis.calculate_mean()))
print('Variance: {:.6f}'.format(analysis.calculate_variance()))
print('Final Volatility metric: {:.6f}'.format(analysis.calculate_volatility()))




# print(obj)