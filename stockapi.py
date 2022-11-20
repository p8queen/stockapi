from pandas_datareader import data as pdr
from datetime import date, timedelta
import yfinance as yf
yf.pdr_override()
import pandas as pd
import numpy as np
import json 
import math

today = date.today()
ticker = 'AAPL'
start_date = today - timedelta(days=30)
end = today
df = pdr.get_data_yahoo(ticker, start=start_date, end=today)

dfr = df.iloc[::-1]
dfr.index = dfr.index.strftime('%m/%d/%Y')
dfr['Day'] = dfr.index
print(dfr.head())
result = dfr.head().to_json(orient="records", index=True)
parsed = json.loads(result)
json_response = json.dumps(parsed, indent=4)
print(json_response)

with open("stockapi.json", "w") as outfile:
    outfile.write(json_response)
    
