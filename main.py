from fastapi import FastAPI, HTTPException, Query
from typing import Annotated
import httpx

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
    
app = FastAPI()

@app.get("/")
async def check():
    return {"check": True}

@app.get("/volatility")
async def get_json_response(
    currency: Annotated[str , Query(
        default= "EUR",
        min_length=3, 
        max_length=3,
        pattern=r"^[a-zA-Z]{3}$")] 
    ):
    url = 'https://api.frankfurter.dev/v1/2026-04-28..2026-05-28?from=USD'

    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json() 
        except httpx.HTTPError:
            raise HTTPException(status_code=502, detail="Failed to fetch external currency data")
        
    analysis = CurrencyAnalyzer()
    try:
        analysis.load_data(data, currency.upper())
    except KeyError:
        raise HTTPException(status_code=422, detail=f"Currency code '{currency}' is invalid or unavailable.")
    
    return {
        "Currency": currency.upper(),
        "total_days_analyzed": analysis.get_total_days(),
        "volatility": round(analysis.calculate_volatility(), 6)
    }

