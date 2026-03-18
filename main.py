from api import api_moeda
from uteis import leiaint,leiafloat

def conversao_taxa(valor,destino):
    dados = api_moeda()

    if destino not in dados['conversion_rates']:
        print('Esse tipo de moeda não existe!')
        return

    taxa = valor * (dados['conversion_rates'][destino])
    return taxa

def main():
    while True:
        print('1 - Converter moeda')
        print('2 - Sair')
        opcao = leiaint('escolha uma opção: ')
        if opcao == 1:
            valor = leiafloat('valor: ')
            destino = input('digite o tipo de moeda: ').strip().upper()
            if destino is None:
                print('Erro, não pode deixar vazio!')
                continue
            resposta = conversao_taxa(valor,destino)
            if resposta:
                print(f"O valor convertido é {resposta:.2f}")
        elif opcao == 2:
            print('Saindo do sistema . . .')
            break
        else:
            print('Opção inválida! ')


main()




