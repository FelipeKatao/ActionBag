import pandas_datareader
import datetime
import yfinance as yf
import pandas as pd
import json

def CdiConsultData(CdiData,valoresARecuperar): 
  # url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(CdiData)
   url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados/ultimos/{}?formato=json'.format(CdiData,valoresARecuperar)
   df = pd.read_json(url)
   print(df) 
   print("execute all")
   pass  
       
def ConsultarIndice(indice,periodo):
  lmt = yf.Ticker(indice)
  hist = lmt.history(period=periodo)
  today = datetime.date.today()
  getData = today.strftime('%Y-%m-%d')
  getData2 = today.strftime('%Y')
  getdata3 = today.strftime("%m")
  data = pandas_datareader.get_data_yahoo(indice,start=getData2+"-"+getdata3+"-01",end=getData)
  print(data.reset_index().to_json(None,orient='records',date_format='iso'))
  jsonData = data.reset_index().to_json(None,orient='records',date_format='iso')
  with open(jsonData) as f:
    datax = json.load(f)
  print(datax)
  print(data.values)
  return data 

def ConsultarIndiceData(indice,periodo,encerramento):
  lmt = yf.Ticker(indice)
  hist = lmt.history(period=periodo)
  today = datetime.date.today()
  getData = today.strftime('%Y-%m-%d')
  getData2 = today.strftime('%Y')
  getdata3 = today.strftime("%m")
  print(getData2+"")
  print(getData)
  data = pandas_datareader.get_data_yahoo(indice,start=getData2+"-"+getdata3+"-01",end=getData)
  
  return data 
 
