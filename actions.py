import yfinance as yf
import pandas as pd

lmt = yf.Ticker("PETR4.SA")  #Tickets da entidade que se deseja buscar

#lmt.info
hist = lmt.history(period="2022") #Data de agora 
#ist = lmt.history(period="1mo")  # Data Referente a um mês

print(hist)

def CdiConsultData(CdiData,valoresARecuperar):
  # url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(CdiData)
   url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados/ultimos/{}?formato=json'.format(CdiData,valoresARecuperar)
   df = pd.read_json(url)
   print(df)

CdiConsultData(12,2)