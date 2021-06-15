from pandas_datareader import data as pdr
from datetime import date, timedelta
import yfinance as yf
yf.pdr_override()
import pandas as pd
import csv


stock_list = ['MSFT','SPY','QQQ','AAPL','GOOG']


filename = 'stock_data.csv'
start_date = '2020-01-01'
end_date = date.today() + timedelta(days = 1)

with open(filename,'w',newline='') as outcsv:
  writer = csv.writer(outcsv)
  writer.writerow(['Date','stock','value','change'])

def getData(stock,filename,start_date,end_date):
  stockData = pdr.get_data_yahoo(stock,start=start_date,end=end_date)
  stockData.insert(1,'Stock',stock)
  stockData['Change'] = stockData['Open'] - stockData['Close'] 
  stockData.reset_index(inplace=True)
  stockData = stockData.rename(columns = {'Stock': 'stock','Open': 'value', 'Change': 'change'})
  with open(filename,'a') as csv_file:
    stockData.to_csv(columns=['Date','stock','value','change'], path_or_buf=csv_file, header=None)  

for stock in stock_list:
  getData(stock, filename, start_date, end_date)



