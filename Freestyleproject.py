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

    todaytest = str(input("Would you like to end the search today? (Y/N)"))
    todaytest = todaytest.lower()
    if todaytest == "y":
        end = date.today()
    else:
        end_year = int(input ("Ending Year of Quote: "))
        end_month = int(input ("Ending Month of Quote: "))
        end_day = int(input ("Ending Day of Quote: "))
        end = datetime.datetime(end_year, end_month, end_day)

    lookup = web.DataReader(symbol, 'yahoo', start, end)

    print(lookup)

    Specific_data_test = str(input("Would you like to save to CSV? (Y/N)"))
    Specific_data_test = Specific_data_test.lower()

    if Specific_data_test == "n":
        print("Thank you for your search")
    else:
        other_path = "Single Day Return.csv"
        with open(other_path, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["Date","Open","high","Low","Close","Adj Close","Volume"])
            writer.writeheader() # uses fieldnames set above
            for date in lookup:
                writer.writerow(date)


def div_Split ():
    start_year = int(input ("Start Year of Quote: "))
    start_month = int(input ("Start Month of Quote: "))
    start_day = int(input ("Start Day of Quote: "))
    start = datetime.datetime(start_year, start_month, start_day)

    todaytest = str(input("Would you like to end the search today? (Y/N)"))
    todaytest = todaytest.lower()
    if todaytest == "y":
        end = date.today()
    else:
        end_year = int(input ("Ending Year of Quote: "))
        end_month = int(input ("Ending Month of Quote: "))
        end_day = int(input ("Ending Day of Quote: "))
        end = datetime.datetime(end_year, end_month, end_day)

    lookup = web.DataReader(symbol, 'yahoo-dividends', start, end)
    print(lookup)

def daily_close ():
    start = str(date.today() - timedelta(days=15)) #> '2017-07-09'
    end = str(date.today())
    lookup = web.DataReader(symbol, 'yahoo', start, end)
    print (lookup)

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

start = []
end = []

ActFunction = "div"
symbol = 'AAPL'

if ActFunction == "single":
    histreturn ()
elif ActFunction == "div":
    div_Split ()
elif ActFunction == "close":
    daily_close ()
else:
    print("Done")
