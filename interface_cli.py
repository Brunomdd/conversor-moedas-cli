from api import api_moeda
from uteis import carregar
from datetime import datetime

def linha(t=32):
    """
    Retorna uma linha de separação composta por traços.

    Parâmetros:
    ----------
    t : int, opcional
        Quantidade de traços na linha. Padrão é 32.

    Retorna:
    -------
    str
        Linha de separação com 't' traços.
    """
    return '-' * t

def cabecalho(txt):
    """
    Exibe um cabeçalho centralizado com linhas acima e abaixo do texto.

    Parâmetros:
    ----------
    txt : str
        Texto que será exibido no cabeçalho.

    Retorna:
    -------
    None
    """
    print(linha())
    print(f'{txt}'.center(32))
    print(linha())

def moedas_disponiveis():
    """
    Exibe todas as moedas disponíveis obtidas via API.

    A função busca as taxas de câmbio da moeda USD e lista todas as moedas
    disponíveis no formato de sigla (ex: USD, BRL, EUR).

    Retorna:
    -------
    None
    """
    cabecalho("MOEDAS DISPONÍVEIS")

    dados = api_moeda("USD")
    if not dados:
        return

    print("Moedas disponíveis (ex: use no formato USD, BRL, EUR)")
    quantidade = len(dados['conversion_rates'])
    print(f"Total: {quantidade}")
    c = 0
    for relatorio in dados['conversion_rates']:
        c += 1
        print(f'{relatorio}', end=' ')
        if c >= 4:
            print('\n')
            c = 0

def ver_historico(lista=None):
    """
    Exibe o histórico de conversões.

    Se nenhum histórico for fornecido, carrega o histórico salvo em arquivo.

    Parâmetros:
    ----------
    lista : list, opcional
        Lista de registros de histórico de conversão. Cada item é um dicionário.
        Se None, a função carrega o histórico do arquivo.

    Retorna:
    -------
    None
    """
    if lista is None:
        lista = carregar()
    if not lista:
        print('Não há nada para mostrar no histórico')
        return

    for valor, item in enumerate(lista, start=1):
        print(linha())
        print(f"{valor}".center(32))
        print(f" Moeda origem: {item['moeda_origem']}".center(32))
        print(f"Moeda destino: {item['moeda_destino']}".center(32))
        print(f'valor original: {item["valor_conversão"]}'.center(32))
        print(f"valor convertido: {item['valor_convertido']}".center(32))
        print(f"Data da conversão: {item.get('data', 'data não disponível')}")

def ordenar_historico(lista=None):
    """
    Retorna o histórico de conversões ordenado por data (mais recente primeiro).

    Parâmetros:
    ----------
    lista : list, opcional
        Lista de registros de histórico. Se None, carrega do arquivo.

    Retorna:
    -------
    list
        Lista ordenada de histórico de conversões.
    """
    if lista is None:
        lista = carregar()

    def pegar_data(item):
        data_str = item.get('data')
        if data_str:
            try:
                return datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
            except ValueError:
                pass
        return datetime(1900, 1, 1)

    lista_ordenada = sorted(lista, key=pegar_data, reverse=True)
    return lista_ordenada

def filtrar_moeda(origem, destino):
    """
    Filtra o histórico de conversões por moeda de origem e destino.

    Parâmetros:
    ----------
    origem : str
        Sigla da moeda de origem (ex: 'BRL').
    destino : str
        Sigla da moeda de destino (ex: 'USD').

    Retorna:
    -------
    list
        Lista de registros que correspondem ao filtro.
    """
    lista = carregar()
    return [i for i in lista if origem == i['moeda_origem'] and destino == i['moeda_destino']]