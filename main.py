from uteis import leiaint,leiafloat,carregar,salvar,confirmar_acao
from conversor import conversao_taxa
from interface_cli import moedas_disponiveis,ver_historico

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
            origem = input('Moeda de origem ex (BRL,EUR,USD): ').strip().upper()
            if not origem or len(origem)!= 3:
                print('Erro moeda de origem inválida')
                continue
            destino = input('Moeda de destino ex (BRL,EUR,USD):  ').strip().upper()
            if not destino or len(destino) != 3:
                print(f'Erro, moeda de destino inválida')
                continue

            valor = leiafloat('valor: ')
            if valor <= 0:
                print('Digite um número maior do que 0.')
                continue

            resposta = conversao_taxa(valor,origem,destino)
            if resposta is None:
                print('Erro ao converter a moeda')
            else:
                print(f"{valor} {origem} → {resposta} {destino}")
                lista.append({'moeda_origem':origem,'moeda_destino':destino,"valor_conversão":valor,"valor_convertido":resposta})
                salvar(lista)

        elif opcao == 2:
            moedas_disponiveis()
        elif opcao == 3:
            ver_historico()
        elif opcao == 4:
            if lista:
                resp = confirmar_acao("Quer continuar? [S/N]")
                if resp == 'N':
                    print('Manteremos o estado atual do seu arquivo.')
                else:
                    print('O historico foi limpo com sucesso!✅')
                    salvar([])
            else:
                print('Não há nada para limpar no historico!❌')
        elif opcao == 5:
            salvar(lista)
            print('Saindo do sistema . . .')
            break
        else:
            print('Opção inválida!')

main()




