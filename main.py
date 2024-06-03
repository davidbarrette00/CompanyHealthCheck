from repository import alpha_vantage_repository, constants

tickers = [
    # "TSLA",
    # "GOOG",
    # "MSFT",
    "USB",
    # "BAC",
    # "CAT",
    # "MCD"
]

for ticker in tickers:
    # overview_data = alpha_vantage_repository.get_overview(ticker)
    sentiment_data = alpha_vantage_repository.get_sentiment(ticker)
    if 'Information' in sentiment_data:
        raise Exception("ERROR: Out of calls for the day")

    # alpha_vantage_repository.append_to_csv(ticker, overview_data, constants.csv_overview)
    alpha_vantage_repository.append_to_csv(ticker, sentiment_data, constants.csv_sentiment)
    print("Data Gathered Successfully for: ", ticker)

print("Sending data to Model")

