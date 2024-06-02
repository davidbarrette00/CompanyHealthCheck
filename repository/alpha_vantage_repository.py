import csv
import os

import requests

from repository import constants

api_key = "RR3S42MPJ3Z9NJ0Q"



def get_overview(symbol):
    if type_check(symbol):
        url = constants.url_overview.replace('SYMBOL', symbol)
        return send_request(url)

def get_income_statement(symbol):
    if type_check(symbol):
        url = constants.url_income_statement.replace('SYMBOL', symbol)
        return send_request(url)

def get_balance_sheet(symbol):
    if type_check(symbol):
        url = constants.url_balance_sheet.replace('SYMBOL', symbol)
        return send_request(url)

def get_cash_flow(symbol):
    if type_check(symbol):
        url = constants.url_cash_flow.replace('SYMBOL', symbol)
        return send_request(url)

def get_earnings(symbol):
    if type_check(symbol):
        url = constants.url_earnings.replace('SYMBOL', symbol)
        return send_request(url)

def get_sentiment(symbol):
    if type_check(symbol):
        url = constants.url_sentiment.replace('SYMBOL', symbol)
        return send_request(url)


def send_request(url):
    return requests.get(url).json()

def type_check(symbol):
    if isinstance(symbol, str):
        return True
    else:
        print("ERROR: symbol must be of type str")
        return False


def append_to_csv(ticker, data, type_of_csv):
    print("Appending to CSV:", type_of_csv)
    if ticker is None:
        print("ERROR: ticker must not be None")
        return
    if data is None:
        print("ERROR: repository must not be None")
        return

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '')) + "\\data\\"+type_of_csv+".csv"
    new_file = False
    if not os.path.exists(path):
        new_file = True

    with open(path, 'a', newline='') as file:
        writer = csv.writer(file)

        match type_of_csv:
            case constants.csv_overview:
                if new_file:
                    writer.writerow(constants.overview_columns)
                writer.writerow(clean_overview_data(data))

            case constants.csv_sentiment:
                if new_file:
                    writer.writerow(constants.sentiment_columns)
                writer.writerow(clean_sentiment_data(ticker, data))



def clean_overview_data(data):
    print("Cleaning overview data")
    data_for_csv = []
    for key in constants.overview_columns:
        data_for_csv.append(data[key])

    return data_for_csv

def clean_sentiment_data(ticker, data):
    print("Cleaning sentiment data")
    data_for_csv = []
    for article in data['feed']:
        for company_sentiment in article['ticker_sentiment']:
            if company_sentiment['ticker'] == ticker:
                for key in constants.sentiment_columns:
                    data_for_csv.append(company_sentiment[key])
                break

    return data_for_csv
