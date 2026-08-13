# pip install yfinance

import yfinance

# get the current stock information about a symbol
data = yfinance.download('AAPL')
print(data)