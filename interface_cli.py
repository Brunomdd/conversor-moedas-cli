from api import  api_moeda
from uteis import carregar
from datetime import  datetime

def moedas_disponiveis():
    dados = api_moeda("USD")
    if not dados:
        print('A APi não conseguiu se conectar ,tente novamente mais tarde')
        return

    quantidade = len(dados['conversion_rates'])
    print(f'Temos ({quantidade}) moedas disponiveis')
    for relatorio in sorted(dados['conversion_rates']):
        print(f'{relatorio}')

def ver_historico(lista=None):
    if lista is None:
        lista = carregar()

    for item in lista:
        print()
        print(f"Moeda origem: {item['moeda_origem']}".center(32))
        print(f"Moeda destino: {item['moeda_destino']}".center(32))
        print(f'valor original: {item['valor_conversão']}'.center(32))
        print(f"valor convertido: {item['valor_convertido']}".center(32))
        print(f"Data da conversão: {item.get('data','data não disponivel')}")
        print()

def ordenar_historico():
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