from pandas_datareader import data
from pandas_datareader.data import DataReader
from datetime import date, timedelta
import pandas_datareader.data as web
import datetime
import csv


def histreturn ():
    start_year = int(input ("Start Year of Quote: "))
    start_month = int(input ("Start Month of Quote: "))
    start_day = int(input ("Start Day of Quote: "))
    start = datetime.datetime(start_year, start_month, start_day)

    end_month = int(input ("Ending Month of Quote: "))
    end_day = int(input ("Ending Day of Quote: "))
    end = datetime.datetime(end_year, end_month, end_day)

    lookup = web.DataReader(symbol, 'yahoo', start, end)


def div_Split ():
    start_year = int(input ("Start Year of Quote: "))
    start_month = int(input ("Start Month of Quote: "))
    start_day = int(input ("Start Day of Quote: "))
    start = datetime.datetime(start_year, start_month, start_day)

    end_month = int(input ("Ending Month of Quote: "))
    end_day = int(input ("Ending Day of Quote: "))
    end = datetime.datetime(end_year, end_month, end_day)

    lookup = web.DataReader(symbol, 'yahoo-dividends', start, end)
    print(lookup)


def compare_stocks ():
    stocks_to_compare = int(input("How many stocks would you like to compare? "))

    stocks_symbols = list()

    start_year = int(input ("Start Year of Quote: "))
    start_month = int(input ("Start Month of Quote: "))
    start_day = int(input ("Start Day of Quote: "))
    start = datetime.datetime(start_year, start_month, start_day)

    end_month = int(input ("Ending Month of Quote: "))
    end_day = int(input ("Ending Day of Quote: "))
    end = datetime.datetime(end_year, end_month, end_day)

    for i in range(int(stocks_to_compare)):
        user_stock_symbols = str(input("Please enter a stock symbol "))
        user_stock_symbols = user_stock_symbols.upper()

        stocks_symbols.append(str(user_stock_symbols))

    lookup = web.DataReader(stocks_symbols, 'yahoo', start, end)

    daily_closing_prices = lookup.ix["Close"]

    print(daily_closing_prices)


print("""
Available Functions:
Single Day Return               (Single)
Dividends and date of issuance  (Div)
Compare two stocks              (Compare)
""")

ActFunction = input("Please Specify which function you want: ")
ActFunction = ActFunction.lower()
symbol = str(input("Please enter the stock ticker: "))
symbol = symbol.upper()

start = []
end = []


if ActFunction == "single":
    histreturn ()
elif ActFunction == "div":
    div_Split ()
elif ActFunction == "compare":
    compare_stocks ()
else:
    print("Done")
