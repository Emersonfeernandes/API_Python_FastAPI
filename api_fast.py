from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

@app.get('/')
def hello():
    return 'Olá mundo!'


class Resp(BaseModel):
    valor1 = int(input('digite número: '))
    valor2 = int(input('digite número: '))
    operaçao = str(input('qual operaçao? '))
    if operaçao == 'adição':
        resultado = valor1 + valor2
    elif operaçao == 'subtração':
        resultado = valor1 - valor2
    elif operaçao == 'divisão':
        try:
           resultado = valor1 / valor2
        except ZeroDivisionError:
           pass
    elif operaçao == 'multiplicação':
        resultado = valor1*valor2

    valor1 : int
    valor2 : int
    operaçao : str
    resultado : int

dados = [
    Resp(valor1=0, valor2=0, operaçao='soma', resultado=0)
]

@app.post('/operacao')
def operacao(resp:Resp):
    dados.append(resp)
    return resp
