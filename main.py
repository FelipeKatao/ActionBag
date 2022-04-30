from argparse import Action
import argparse
from datetime import date
import pandas
import numpy as np
import pandas as pd
import actions as ac
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=["GET"])
def main():
    variavel =  "ticket"
    return render_template("index.html", variavel = variavel)

@app.route('/acao/<string:ticket>')       
def ticketload(ticket):
    ticketSet = ticket  
    ticketname = ticket
    ticketnameSet = ticketname 
    ticketRead = ac.ConsultarIndice(ticket,'1y')
    return render_template("tickets.html",ticketSet = ticketRead,ticketname = ticketnameSet )

@app.route('/acao/<string:ticket>')       
def ticketloadPeriod(ticket):
    ticketRead = ac.ConsultarIndice(ticket,0)  
    return render_template("tickets.html",ticketSet = ticketRead)

@app.route('/acao')       
def ticketlist(): 
    return render_template("acao.html") 

@app.route('/dashboard/<string:ticket1>/<string:ticket2>/<string:ticket3>')
def dashboard(ticket1,ticket2,ticket3):
    ticketRead1 = ac.getVolumeTotal(ticket1)
    ticketRead2 = ac.getVolumeTotal(ticket2)
    ticketRead3 = ac.getVolumeTotal(ticket3)
    aberturaFechamento = [[ticket1,ac.getAbertura(ticket1),ac.getFechamento(ticket1)],[ticket2,ac.getAbertura(ticket2),ac.getFechamento(ticket2)],[ticket3,ac.getAbertura(ticket3),ac.getFechamento(ticket3)]]
    VolumeTicketsTotal = [[ticket1,ticketRead1],[ticket2,ticketRead2],[ticket3,ticketRead3]]
    return render_template("dashboard.html",ticket1=ticket1,ticket2=ticket2,ticket3=ticket3,VolumeTicketsTotal=VolumeTicketsTotal,aberturaFechamento=aberturaFechamento)   

@app.route('/acao/<string:ticket>/<string:dateInit>/<string:dateEnd>')
def ticketPeriodDate(ticket,dateInit,dateEnd):
    ticketname = ticket
    print("ticket")
    ticketRead = ac.ConsultarIndiceData(ticket,dateInit,dateEnd)
    return render_template("tickets.html",ticketSet=ticketRead,dateInit=dateInit,dateEnd=dateEnd,ticketname = ticketname)  
@app.route('/result/<string:ticket>')
def ticketResults(ticket): 
    ticketName = ticket
    ticketResultData = int(ac.consultarRentabilidadeIndice(ticket))
    valorCompra = ac.compraInicial(ticket)
    valorCompra = f'{valorCompra:.2f}'
    volume = ac.getVolumeFinalInicial(ticket)
    return render_template("tickets.html",ticketName = ticketName,ticketResultData = ticketResultData,valorCompra=valorCompra,volume=volume)
@app.route('/<string:nome>')
def error(nome):         
    variavel =nome
    print(variavel)
    return render_template("error.html", variavel = variavel)  

if __name__ == "__main__":
   port = int(os.environ.get('PORT', 5000))
   app.run(use_debugger=False, use_reloader=True, passthrough_errors=True,port=port)   
