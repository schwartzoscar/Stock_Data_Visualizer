import requests
import app

# In the code below we first set the api to the SetApi function in app.py. We then use the information returned from the UI to
# get the symbol of the stock data the user is wishing to view, before running it through the url variable with retrieves
# the data from the API.

# To access one of these variables you will first need to use the following example,
#import app
#stock_data = app.GetStock()
#symbol = stock_data["symbol"]

def pullStock():
    interval = "&interval=15min" if app.GetTimeSeries() == "TIME_SERIES_INTRADAY" else ""
    url = f"https://www.alphavantage.co/query?function={app.GetTimeSeries()}&symbol={app.GetStockSymbol()}{interval}&apikey={app.GetApi()}"
    r = requests.get(url)
    data = r.json()
    app.SetStock(data)
# })



