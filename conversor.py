from api import api_moeda
def conversao_taxa(valor,origem,destino):
    dados = api_moeda(origem)
    if not dados:
        print('A APi não conseguiu se conectar ,tente novamente mais tarde')
        return
    if origem == destino:
        print('Não é possivel converter uma mesma moeda!')
        return

    if len(destino) !=3 :
        print('formato de moeda dever ser com 3 Caracteres! ')
        return

    if destino not in dados['conversion_rates']:
        print('Esse tipo de moeda não existe!')
        return

    taxa = valor * (dados['conversion_rates'][destino])
    return taxa
