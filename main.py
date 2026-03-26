from uteis import leiaint,leiafloat,carregar,salvar,confirmar_acao
from conversor import conversao_taxa
from interface_cli import moedas_disponiveis,ver_historico,ordenar_historico,linha,cabecalho
from datetime import  datetime

def filtrar_moeda(origem):
    lista = carregar()
    filtro = []

    for i in lista:
        if origem == i['moeda_origem']:
            filtro.append(i)
    return filtro

def main():
    lista = carregar()
    while True:
        print(linha())
        print('1 - Converter moeda')
        print('2 - Listar moedas disponiveis')
        print('3 - Ver historico')
        print('4 - Limpar Histórico ')
        print('5 - Ver historico ordenado')
        print('6 - Filtrar historico por moeda')
        print('7 - Sair')
        print(linha())

        opcao = leiaint('escolha uma opção: ')
        if opcao == 1:
            agora = datetime.now()
            data_hora_br = agora.strftime("%d/%m/%Y %H:%M:%S")
            origem = input('Moeda de origem ex (BRL,EUR,USD): ').strip().upper()
            if not origem or len(origem)!= 3:
                print('Erro moeda de origem inválida')
                continue
            destino = input('Moeda de destino ex (BRL,EUR,USD):  ').strip().upper()
            if not destino or len(destino) != 3:
                print(f'Erro: moeda inválida (use 3 letras, ex: USD)')
                continue
            valor = leiafloat('valor: ')
            if valor <= 0:
                print('Digite um número maior do que 0.')
                continue
            resposta = conversao_taxa(valor,origem,destino)
            if resposta is None:
                print('Erro ao converter a moeda')
            else:
                print(f"{valor} {origem} → {resposta:.2f} {destino} (salvo no histórico ✅)")
                lista.append({'moeda_origem':origem,'moeda_destino':destino,"valor_conversão":valor,"valor_convertido":resposta,'data':data_hora_br})
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
                    lista.clear()
                    print('O historico foi limpo com sucesso!✅')
                    salvar(lista)
            else:
                print('Não há nada para limpar no historico!❌')
        elif opcao == 5:
            lista_ordenada = ordenar_historico()
            if lista_ordenada is None:
                print('Não há nada para mostrar')
            else:
                ver_historico(lista_ordenada)

        elif opcao == 6:
            origem = input('Moeda de origem ex (BRL,EUR,USD): ').strip().upper()
            filtro = filtrar_moeda(origem)
            if not filtro:
                print(f'nenhum filtro encontrado para {origem}')
            else:
                filtro = filtrar_moeda(ver_historico)

        elif opcao == 7:
             salvar(lista)
             cabecalho("Saindo do sistema . . .")
             break
        else:
            print('Opção inválida!')

main()




