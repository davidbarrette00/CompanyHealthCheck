from repository import alpha_vantage_repository, constants
import connect_to_claude

import csv
import os


tickers = [
    # "TSLA",
    # "GOOG",
    # "MSFT",
    # "USB",
    # "BAC",
    # "CAT",
    # "MCD"
]

# for ticker in tickers:
#     # overview_data = alpha_vantage_repository.get_overview(ticker)
#     sentiment_data = alpha_vantage_repository.get_sentiment(ticker)
#     if 'Information' in sentiment_data:
#         raise Exception("ERROR: Out of calls for the day")
#
#     # alpha_vantage_repository.append_to_csv(ticker, overview_data, constants.csv_overview)
#     alpha_vantage_repository.append_to_csv(ticker, sentiment_data, constants.csv_sentiment)
#     print("Data Gathered Successfully for: ", ticker)
#
# print("Sending data to Model")

path = os.path.abspath(os.path.dirname(__file__)) + "\\data\\" + constants.csv_overview + ".csv"
if os.path.exists(path):
    with open(path, 'r', newline='') as file:
        reader = csv.reader(file)
        columns = next(reader)
        values = next(reader)

        message_for_claude = ""
        for column, value in zip(columns, values):
            message_for_claude += "{}: {}, ".format(column, value)
        message_for_claude = constants.ai_overview_prompt + message_for_claude[:-2]

        print(connect_to_claude.send_message(message_for_claude))
else:
    print("File {} does not exist".format(path))
