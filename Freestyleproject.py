from pandas_datareader import data
from pandas_datareader.data import DataReader
from datetime import date, timedelta
import pandas_datareader.data as web
import datetime
import csv

def start_date ():
    start_year = int(input ("Start Year of Quote: "))
    start_month = int(input ("Start Month of Quote: "))
    start_day = int(input ("Start Day of Quote: "))
    start = datetime.datetime(start_year, start_month, start_day)

def end_date ():
    end_year = int(input ("Ending Year of Quote: "))
    end_month = int(input ("Ending Month of Quote: "))
    end_day = int(input ("Ending Day of Quote: "))
    end = datetime.datetime(end_year, end_month, end_day)

def end_today ():
    todaytest = str(input("Would you like to end the search today? (Y/N)"))
    todaytest = todaytest.lower()
    if todaytest == "y":
        end = date.today()
    else:
        end_date()

def histreturn ():
    start_year = int(input ("Start Year of Quote: "))
    start_month = int(input ("Start Month of Quote: "))
    start_day = int(input ("Start Day of Quote: "))
    start = datetime.datetime(start_year, start_month, start_day)
    end_year = int(input ("Ending Year of Quote: "))
    end_month = int(input ("Ending Month of Quote: "))
    end_day = int(input ("Ending Day of Quote: "))
    end = datetime.datetime(end_year, end_month, end_day)

    lookup = web.DataReader(symbol, 'yahoo', start, end)

    print(lookup)

    Specific_data_test = str(input("Would you like to tease out specific data? (Y/N)"))
    Specific_data_test = Specific_data_test.lower()

    if Specific_data_test == "n":
        print("hokay no data")
    else:
        print("""
Please specify the data you would like to print:
Open, High, Low, Close, Adj Close, Volume
            """)
    quote = lookup.ix[start]


def Div_Split ():
    start_date()
    end_today()
    lookup = web.DataReader(symbol, 'yahoo-dividends', start, end)
    print(lookup)

# print("""
# Available Functions:
# Single Day Return               (Single)
# Dividends and date of issuance  (Div)
# List of Daily Closes            (Close)
# """)
#
# ActFunction = input("Please Specify which function you want: ")
# ActFunction = ActFunction.lower()
# symbol = str(input("Please enter the stock ticker: "))
# symbol = symbol.upper()

ActFunction = "single"
symbol = 'AAPL'

if ActFunction == "single":
    histreturn()
if ActFunction == "div":
    Div_Split ()
else:
    print("Done")
