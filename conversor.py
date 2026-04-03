from api import api_moeda

def conversao_taxa(valor, origem, destino):
    """
    Converte um valor de uma moeda de origem para uma moeda de destino
    utilizando taxas de câmbio obtidas via API externa.

    A função retorna `None` em casos de:
        - Moeda de origem e destino iguais.
        - Siglas de moedas inválidas (não com 3 letras).
        - Falha na obtenção de dados da API.
        - Moeda de destino não disponível na API.

    Parâmetros:
    ----------
    valor : float
        Valor a ser convertido. Deve ser maior que 0.
    origem : str
        Sigla da moeda de origem (ex: 'BRL', 'USD', 'EUR').
    destino : str
        Sigla da moeda de destino (ex: 'BRL', 'USD', 'EUR').

    Retorna:
    -------
    float ou None
        Valor convertido arredondado para 2 casas decimais, ou None se houver erro.
    """
    origem = origem.upper()
    destino = destino.upper()

    if origem == destino:
        return None
    if len(origem) != 3 or len(destino) != 3:
        return None

    dados = api_moeda(origem)
    if not dados or 'conversion_rates' not in dados:
        return None

    if destino not in dados['conversion_rates']:
        return None

    valor_convertido = round(valor * dados['conversion_rates'][destino], 2)
    return valor_convertido