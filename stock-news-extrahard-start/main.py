import requests
from twilio.rest import Client

# importing stock price with api
STOCK = "TSLA"
ACCOUNT_SID = "ACfc5672db37b86b7101318c7e6c69faff"
AUTH_TOKEN = "3dc06b2db42706941d487c370ba34440"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "D3ERWU3TFN6DSA8K"
NEWS_API_KEY = "7ee99bd181f042a2822d29e5d2c8ea0e"

news_params = {
    "q": COMPANY_NAME,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}

alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

stock_response = requests.get("https://www.alphavantage.co/query", params=alpha_params)
stock_response.raise_for_status()
daily_stock_data = stock_response.json()["Time Series (Daily)"]
recent_closing_prices = [float(daily_stock_data[date]["4. close"]) for date in daily_stock_data]

pc_price_change = ((recent_closing_prices[1] - recent_closing_prices[2]) / recent_closing_prices[1]) * 100

if pc_price_change >= 5 or pc_price_change <= -5:
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_data = news_response.json()
    recent_news_list = news_data["articles"]
    title_desc_news = [{"title": recent_news_list[index]["title"], "description": recent_news_list[index]["description"]} for index in range(3)]
    print(title_desc_news)
    # creating message:
    for index in range(3):
        news_message = ""
        if pc_price_change >= 5:
            news_message = f"{STOCK}: 🔺{int(pc_price_change)} \nHeadline: {title_desc_news[index]['title']}\nBrief: {title_desc_news[index]['description']}"
        else:
            news_message = f"{STOCK}: 🔻{int(pc_price_change)} \nHeadline: {title_desc_news[index]['title']}\nBrief: {title_desc_news[index]['description']}"

        # Sending the sms to the user
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
            body=news_message,
            from_='+19284474635',
            to='+998915228512'
        )

        print(message.status)
