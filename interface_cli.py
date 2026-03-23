from api import  api_moeda
from uteis import carregar

def moedas_disponiveis():
    dados = api_moeda("USD")
    if not dados:
        print('A APi não conseguiu se conectar ,tente novamente mais tarde')
        return


    quantidade = len(dados['conversion_rates'])
    print(f'Temos ({quantidade}) moedas disponiveis')
    for relatorio in sorted(dados['conversion_rates']):
        print(f'{relatorio}')

def ver_historico():
    historico = carregar()
    if not historico:
        print('Não há nada para mostrar no historico!')
        return
    for item in historico:
        print()
        print(f"Moeda origem: {item['moeda_origem']}".center(32))
        print(f"Moeda destino: {item['moeda_destino']}".center(32))
        print(f'valor original: {item['valor_conversão']}'.center(32))
        print(f"valor convertido: {item['valor_convertido']}".center(32))
        print(f'data da conversão: {item['data']}')
        print()
