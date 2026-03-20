from uteis import leiaint,leiafloat,carregar,salvar,confirmar_acao
from conversor import conversao_taxa
from listar_moedas import moedas_disponiveis,ver_historico

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
            origem = input('Moeda de origem ex (BRL,EU,USD): ').strip().upper()
            if not origem:
                print('Erro não pode deixar vazio!')
                continue
            destino = input('Moeda de destino ex (BRL,EU,USD):  ').strip().upper()
            if not origem or not destino:
                print('Erro! o campo não foi preenchido.')
                continue
            valor = leiafloat('valor: ')
            if valor <= 0:
                print('Digite um número maior do que 0.')
                continue

            resposta = conversao_taxa(valor,origem,destino)
            print(f"{valor} {origem} → {resposta:.2f} {destino}")
            lista.append({'moeda_origem':origem,'moeda_destino':destino,"valor_conversão":valor,"valor_convertido":resposta})
            salvar(lista)

        elif opcao == 2:
            moedas_disponiveis()
        elif opcao == 3:
            ver_historico()
        elif opcao == 4:
            limpar = carregar()
            if limpar:
                resp = confirmar_acao("Quer continuar? [S/N]")
                if resp == 'N':
                    print('Manteremos o estado atual do seu arquivo.')
                else:
                    print('O historico foi limpo com sucesso!✅')
                    salvar([])
            else:
                print('Não há nada para limpar no historico!❌')
        elif opcao == 5:
            print('Saindo do sistema . . .')
            break
        else:
            print('Opção inválida!')

main()




