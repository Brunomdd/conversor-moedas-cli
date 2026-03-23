from api import api_moeda
def conversao_taxa(valor,origem,destino):
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

    valor_convertido = round(valor * dados['conversion_rates'][destino],2)
    return valor_convertido
