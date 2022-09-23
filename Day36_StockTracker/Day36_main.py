from twilio.rest import Client
from datetime import date, timedelta
import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
av_api_key = "SECRETS"
news_api_key = "SECRETS"
twilio_api_key = "SECRETS"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def stock_diff_finder():
    #Find yesterday and 2 days ago dates
    yesterday_date = str(date.today() - timedelta(1))
    twodaysprev_date = str(date.today() - timedelta(2))

    #parameters for alphavantage api
    stock_parameters = {
        "function":"TIME_SERIES_DAILY",
        "symbol":"TSLA",
        "outputsize":"compact",
        "datatype":"json",
        "apikey":"SECRETS"
    }

    #getting the requests response and the closing prices
    stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
    stock_data = stock_response.json()
    yesterday_closing = float(stock_data["Time Series (Daily)"][yesterday_date]["4. close"])
    twodaysprev_closing = float(stock_data["Time Series (Daily)"][twodaysprev_date]["4. close"])

    percent_diff = round((abs(yesterday_closing - twodaysprev_closing) / ((yesterday_closing + twodaysprev_closing) / 2)) * 100, 2)

    #calculating the differences
    if yesterday_closing > twodaysprev_closing:
        return("🔻", percent_diff)
    else:
        return("🔺", percent_diff)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def news_finder():
    news_articles = []
    news_parameters = {
        "q":"Tesla",
        "searchin":"title",
        "language":"en",
        "apiKey":"SECRETS"
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params = news_parameters)
    print(news_response.status_code)
    news_data = news_response.json()
    for x in range(0,3):
        news_title = news_data["articles"][x]["title"]
        news_desc = news_data["articles"][x]["description"]
        news_articles.append([news_title, news_desc])

    return news_articles


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_text(change_arrow, percent_change, news_articles):
    account_sid = 'SECRETS'
    auth_token = 'SECRETS'
    for x in range(0,3):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"TSLA {change_arrow} {percent_change}%\nHeadline: {news_articles[x][0]}\nBrief Desc: {news_articles[x][1]}",
            from_='+SECRETS',
            to='+SECRETS'
        )
    print(message.status)

arrow_direction, percent_difference = stock_diff_finder()
if percent_difference > 3:
    news_articles = news_finder()
    send_text(arrow_direction, percent_difference, news_articles)
