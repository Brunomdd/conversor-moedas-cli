import json
from json import  JSONDecodeError

def confirmar_acao(msg):
    while True:
        resp = str(input(msg)).strip().upper()
        if resp in ('S','N'):
            return  resp


def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('erro! digite um número inteiro!')


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('erro! digite um número float!')


from json import  JSONDecodeError

def carregar():
    lista = []
    try:
        with open("history.json","r",encoding="utf-8") as arq:
            return json.load(arq)
    except (FileNotFoundError,JSONDecodeError):
        lista = []
    return lista

def salvar(lista):
    with open("history.json","w",encoding='utf-8') as arq:
        json.dump(lista,arq,ensure_ascii= False,indent=4)

