from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd

ticker_list = ['DJIA','DOW','LB','EXPE','PXD','MHCP','CRM','JEC','NRG','HFC','NOW']

today=date.today()

start_date='2019-11-30'
end_date = '2021-5-31'

files=[]
def getData(ticker):
    print(ticker)
    data=pdr.get_data_yahoo(ticker,start=start_date,end=today)
    dataname=ticker+'_'+str(today)
    files.append(dataname)
    SaveData(data,dataname)

def SaveData(df,filename):
    df.to_csv('./data/'+filename+'.csv')

#for tik in ticker_list:
 #   getData(tik)
#for i in range(0,10):
 #   df1 = pd.read_csv('./data/'+str(files[i])+'.csv')
  #  print(df1.head())

stock = 'MSFT'
data = pdr.get_data_yahoo(stock,start=start_date,end=end_date)
#get date from header and insert into data
data.insert(1,'Stock',stock)
#print(len(data))
#i = 0 
#stocklist = []
#while i < len(data):
 #   stocklist.append(stock)
  #  i = i+1
#data['Stock'] = stocklist
data['Change'] = data['Open'] - data['Close'] 
data.reset_index(inplace=True)
data = data.rename(columns = {'Stock': 'stock','Open': 'value', 'Change': 'change'})
with open('csv_data.csv','w') as csv_file:
    data.to_csv(columns=['Date','stock','value','change'],path_or_buf=csv_file)
#print(output)