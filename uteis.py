import json
from json import  JSONDecodeError

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
        with open("moeda_historico.json","r",encoding="utf-8") as arq:
            return json.load(arq)
    except (FileNotFoundError,JSONDecodeError):
        lista = []
    return lista

def salvar(lista):
    with open("moeda_historico.json","w",encoding='utf-8') as arq:
        json.dump(lista,arq,ensure_ascii= False,indent=4)

