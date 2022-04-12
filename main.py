from argparse import Action
import pandas
import numpy as np
import pandas as pd
import actions as ac
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main():
    variavel =  "ticket"
    return render_template("index.html", variavel = variavel)

@app.route('/<string:nome>')
def error(nome):
    variavel = f'Pagina ({nome}) não existe'
    return render_template("error.html", variavel = variavel)

if __name__ == "__main__":
    app.run();