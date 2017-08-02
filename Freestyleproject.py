from pandas_datareader import data
from pandas_datareader.data import DataReader
from datetime import date, timedelta
import pandas_datareader.data as web
import datetime



def histreturn ():
    symbol = str(input("Please enter the stock ticker: "))
    start_year = int(input ("Start Year of Quote: "))
    start_month = int(input ("Start Month of Quote: "))
    start_day = int(input ("Start Day of Quote: "))

    todaytest = str(input("Would you like to end the search today? (Y/N)"))
    todaytest = todaytest.lower()

    start = datetime.datetime(start_year, start_month, start_day)

    if todaytest = "y":
        end = date.today()
    else:
        end_year = int(input ("Ending Year of Quote: "))
        end_month = int(input ("Ending Month of Quote: "))
        end_day = int(input ("Ending Day of Quote: "))
        end = datetime.datetime(end_year, end_month, end_day)
        
    lookup = web.DataReader(symbol, 'yahoo', start, end)
    # quote = lookup.ix[start]
    print(lookup)

def Div_Split ():
    start_info ()
    lookup = web.DataReader(symbols, 'yahoo-actions', start, end)
    quote = lookup.ix[end]
    print(quote)

# print("""
# Available Functions:
# Single Day Return               (Single)
# Dividends and Stock Splits      (Div Split)
# List of Daily Closes            (Close)
# """)
#
# ActFunction = input("Please Specify which function you want: ")
# ActFunction = ActFunction.lower()

ActFunction = "single"

if ActFunction == "single":
    histreturn()
elif ActFunction == "div split":
    start = input("Please Enter the date of the quote: ")
    start = str(start)
    datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime(2015, 5, 9)
    output = web.DataReader('AAPL', 'yahoo-actions', start, end)
    print(output)
else:
    print("Done")
