import yfinance as yf

lmt = yf.Ticker("PETR4.SA")  #Tickets da entidade que se deseja buscar

#lmt.info
hist = lmt.history(period="2022") #Data de agora 
#ist = lmt.history(period="1mo")  # Data Referente a um mês

print(hist)