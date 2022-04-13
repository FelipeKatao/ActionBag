import pandas_datareader
import datetime
import yfinance as yf
import pandas as pd

def CdiConsultData(CdiData,valoresARecuperar): 
  # url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(CdiData)
   url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados/ultimos/{}?formato=json'.format(CdiData,valoresARecuperar)
   df = pd.read_json(url)
   print(df) 
   pass  
       
def ConsultarIndice(indice,periodo):
  lmt = yf.Ticker(indice)
  hist = lmt.history(period=periodo)
  data = pandas_datareader.get_data_yahoo(indice,start="2021",end="2022")
  print(data.values)
  return data 
