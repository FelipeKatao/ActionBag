from argparse import Action
import argparse
import pandas
import numpy as np
import pandas as pd
import actions as ac
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

@app.route('/acao/<string:ticket>/<int:year>')       
def ticketloadPeriod(ticket,periodo):
    ticketRead = ac.ConsultarIndice(ticket,periodo)
    return render_template("tickets.html",ticketSet = periodo)

@app.route('/<string:nome>')
def error(nome):       
    variavel =nome
    return render_template("error.html", variavel = variavel)  

if __name__ == "__main__":
   app.run(use_debugger=False, use_reloader=True, passthrough_errors=True) 