from api import  api_moeda
from uteis import carregar
from datetime import  datetime

def linha(t=32):
    return '-' * t

def cabecalho(txt):
    print(linha())
    print(f'{txt}'.center(32))
    print(linha())

def moedas_disponiveis():
    cabecalho("MOEDAS DISPONÌVEIS")

    dados = api_moeda("USD")
    if not dados:
        return

    print("Moedas disponíveis (ex: use no formato USD, BRL, EUR)")
    quantidade = len(dados['conversion_rates'])
    print(f"Total: {quantidade}")
    c = 0
    for relatorio in dados['conversion_rates']:
        c+=1
        print(f'{relatorio}',end=' ')
        if c >=4:
            print('\n')
            c = 0

def ver_historico(lista=None):
    if lista is None:
        lista = carregar()
    if not lista:
        print('Não há nada para mostrar no histórico')
        return

    for valor, item in  enumerate(lista,start=1):
        print(linha())
        print(f"{valor}".center(32))
        print(f" Moeda origem: {item['moeda_origem']}".center(32))
        print(f"Moeda destino: {item['moeda_destino']}".center(32))
        print(f'valor original: {item['valor_conversão']}'.center(32))
        print(f"valor convertido: {item['valor_convertido']}".center(32))
        print(f"Data da conversão: {item.get('data','data não disponivel')}")

def ordenar_historico(lista):
    lista = carregar()
    def pegar_data(item):
        data_str = item.get('data')
        if data_str:
            try:
                return datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
            except ValueError:
                pass
        return datetime(1900,1,1)
    lista_ordenada = sorted(lista,key=pegar_data,reverse=True)
    return  lista_ordenada

def filtrar_moeda(origem,destino):
    lista = carregar()
    filtro = []

    for i in lista:
        if origem == i['moeda_origem'] and destino == i['moeda_destino']:
            filtro.append(i)
    return filtro