from api import api_moeda
from uteis import leiaint,leiafloat,carregar,salvar

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
        print()


def main():
    lista = carregar()
    while True:
        print('1 - Converter moeda')
        print('2 - Listar moedas disponiveis')
        print('3 - Ver historico')
        print('4 - Limpar Histórico ')
        print('5 - Sair')
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
                lista.append({'moeda_origem':origem,'moeda_destino':destino,"valor_conversão":valor,"valor_convertido":resposta})
                salvar(lista)
        elif opcao == 2:
            moedas_disponiveis()
        elif opcao == 3:
            ver_historico()
        elif opcao == 4:
            limpar = carregar()
            if limpar:
                print('O historico foi limpo com sucesso! ✅')
                salvar([])
            else:
                print('Não há nada para limpar no historico!')
        elif opcao == 5:
            print('Saindo do sistema . . .')
            break

        else:
            print('Opção inválida!')

main()




