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

@app.route('/acao/<string:ticket>/<string:dateInit>/<string:dateEnd>')
def ticketPeriodDate(ticket,dateInit,dateEnd):
    ticketname = ticket
    print("ticket")
    ticketRead = ac.ConsultarIndiceData(ticket,dateInit,dateEnd)
    return render_template("tickets.html",ticketSet=ticketRead,dateInit=dateInit,dateEnd=dateEnd,ticketname = ticketname)  

@app.route('/<string:nome>')
def error(nome):        
    variavel =nome
    print(variavel)
    return render_template("error.html", variavel = variavel)  

if __name__ == "__main__":
   port = int(os.environ.get('PORT', 5000))
   app.run(use_debugger=False, use_reloader=True, passthrough_errors=True,port=port)   
