import os


def CalcRenta(Atual,passado):
    valor = int(Atual)/int(passado)
    valor = valor-1
    valor=valor*100
    valor = f'{valor:.0f}%'
    return valor