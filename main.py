from api import api_moeda
from uteis import leiaint,leiafloat

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


def moedas_disponiveis():
    dados = api_moeda("USD")
    if not dados:
        print('A APi não conseguiu se conectar ,tente novamente mais tarde')
        return

    quantidade = len(dados['conversion_rates'])
    print(f'Temos ({quantidade}) moedas disponiveis')
    for relatorio in sorted(dados['conversion_rates']):
        print(f'{relatorio}')


def main():
    while True:
        print('1 - Converter moeda')
        print('2 - Listar moedas disponiveis')
        print('3 - Sair')
        opcao = leiaint('escolha uma opção: ')
        if opcao == 1:
            origem = input('Moeda de origem ex (BRL,EU,USD):').strip().upper()
            destino = input('Moeda de destino: ').strip().upper()
            valor = leiafloat('valor: ')
            if not destino:
                print('Erro, não pode deixar vazio!')
                continue
            resposta = conversao_taxa(valor,origem,destino)
            if resposta:
                print(f"O valor convertido é {resposta:.2f} ")
        elif opcao == 2:
            moedas_disponiveis()
        elif opcao == 3:
            break
        else:
            print('Opção inválida!')


main()




