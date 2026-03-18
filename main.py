from api import api_moeda

def conversao_taxa(valor,tipo):
    dados = api_moeda()
    print(dados)

def main():

    while True:
        opcao = int(input('escolha uma opção: '))
        if opcao == 1:
            valor = float(input('valor: '))
            tipo = input('digite o tipo de moeda: ')
            conversao_taxa(valor,tipo)

main()




