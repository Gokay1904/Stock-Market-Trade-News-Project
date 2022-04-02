
import requests
from _datetime import datetime,timedelta


COMPANY_NAME = "Tesla Inc"

News_API_KEY = "newsapi.org api key"

AlphaVantage_API_KEY = "Alphavantage api key here"

news_params = {"language": "en",
               "sortBy": "popularity",
               "q": COMPANY_NAME
}

market_params = {
               "symbol": "TSLA",
               "slice": "year2month2",
               "function": "TIME_SERIES_DAILY"
}


vantage_url = f'https://www.alphavantage.co/query?apikey={AlphaVantage_API_KEY}'
r1 = requests.get(vantage_url,params=market_params)
stock_data = r1.json()

today = datetime.today()
yesterday = today - timedelta(days = 1) #For getting info of 1 day before. (Because intraday stock market data has not been updated.)

timeSeries = "Time Series (Daily)"




news_url = F"https://newsapi.org/v2/everything?apiKey={News_API_KEY}"
r2 = requests.get(news_url,params=news_params)
news_data = r2.json()

#Method collects 5 Article from newsapi.org if the increase or decrease ratio is more than %5.
def get_news():
    articles = news_data["articles"]
    for article_index in range(1, 6):
        print(f"Article {article_index}")
        print(articles[article_index]["author"])
        print(articles[article_index]["title"])
        print(articles[article_index]["description"])
        print(articles[article_index]["url"], "\n")



def CalculatePriceRange():

    targetDay = yesterday - timedelta(days = 1)

    yesterdays_close_price = stock_data[timeSeries][f"{yesterday.date()}"]["4. close"]
    targetdays_close_price = stock_data[timeSeries][f"{targetDay.date()}"]["4. close"]

    ratio = abs(((float(yesterdays_close_price) - float(targetdays_close_price)) / float(targetdays_close_price)) * 100)

    if(yesterdays_close_price > targetdays_close_price):
        print(f"Price is rising. Increase ratio: ▲ %{ratio}")
        if(ratio >=5):
            get_news()
    elif (yesterdays_close_price < targetdays_close_price):
        print(f"Price is decreasing: ▼ -%{ratio}")
        if(ratio >= 5):
            get_news()

CalculatePriceRange()










