import json

import requests

from data import constants

api_key = "RR3S42MPJ3Z9NJ0Q"

def get_overview(symbol):
    if type_check(symbol):
        url = constants.overview.replace('SYMBOL', symbol)
        return send_request(url)

def get_income_statement(symbol):
    if type_check(symbol):
        url = constants.income_statement.replace('SYMBOL', symbol)
        return send_request(url)

def get_balance_sheet(symbol):
    if type_check(symbol):
        url = constants.balance_sheet.replace('SYMBOL', symbol)
        return send_request(url)

def get_cash_flow(symbol):
    if type_check(symbol):
        url = constants.cash_flow.replace('SYMBOL', symbol)
        return send_request(url)

def get_earnings(symbol):
    if type_check(symbol):
        url = constants.earnings.replace('SYMBOL', symbol)
        return send_request(url)


def send_request(url):
    return requests.get(url).json()

def type_check(symbol):
    if isinstance(symbol, str):
        return True
    else:
        print("ERROR: symbol must be of type str")
        return False