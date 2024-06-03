
#Alpha Vantage Urls
url_overview = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=SYMBOL&apikey=RR3S42MPJ3Z9NJ0Q'
url_income_statement = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=SYMBOL&apikey=RR3S42MPJ3Z9NJ0Q'
url_balance_sheet = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=SYMBOL&apikey=RR3S42MPJ3Z9NJ0Q'
url_cash_flow = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=SYMBOL&apikey=RR3S42MPJ3Z9NJ0Q'
url_earnings = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=SYMBOL&apikey=RR3S42MPJ3Z9NJ0Q'
url_sentiment = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=SYMBOL&apikey=RR3S42MPJ3Z9NJ0Q'

# Types of csv file
csv_overview = "OVERVIEW"
csv_sentiment = "SENTIMENT"

#CSV columns
overview_columns = [
    "Symbol",
    "Sector",
    "Industry",
    "EBITDA",
    "EPS",
    "ProfitMargin",
    "AnalystRatingStrongBuy",
    "AnalystRatingBuy",
    "AnalystRatingHold",
    "AnalystRatingSell",
    "AnalystRatingStrongSell",
    "EVToRevenue",
    "EVToEBITDA",
    "50DayMovingAverage",
    "200DayMovingAverage"
]

sentiment_columns = [
    "ticker",
    "relevance_score",
    "ticker_sentiment_score"
]

#prompts to AI
ai_overview_prompt = "Here is some relevant overview information for a company. Give me a short summary describing " \
                     "the percieved health of the company, finishing with a score between 0 and 1 with 5 significant digits, " \
                     "0 meaning sell the company stock, 0.5 meaning hold the company stock, and 1 meaning buy the company stock: "