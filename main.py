from uteis import leiaint, leiafloat, carregar, salvar, confirmar_acao
from conversor import conversao_taxa
from interface_cli import moedas_disponiveis, ver_historico, ordenar_historico, linha, cabecalho, filtrar_moeda
from datetime import datetime


def main():
    """
    Executa o sistema de conversão de moedas com histórico.

    O programa permite que o usuário:
        1. Converta valores entre diferentes moedas.
        2. Liste as moedas disponíveis.
        3. Consulte o histórico de conversões.
        4. Limpe o histórico.
        5. Veja o histórico ordenado.
        6. Filtre o histórico por moeda de origem e destino.
        7. Saia do sistema, salvando o histórico atual.

    O histórico é carregado no início da execução a partir de um arquivo
    e salvo a cada modificação ou ao sair do sistema.

    O fluxo principal é baseado em um loop interativo que apresenta
    um menu e solicita a escolha do usuário.

    Estrutura do histórico:
        - moeda_origem: str, sigla da moeda de origem (ex: 'BRL')
        - moeda_destino: str, sigla da moeda de destino (ex: 'USD')
        - valor_conversão: float, valor informado para conversão
        - valor_convertido: float, valor convertido
        - data: str, data e hora da conversão no formato DD/MM/AAAA HH:MM:SS

    Não retorna nada.
    """
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
            if not origem or len(origem) != 3:
                print('Erro moeda de origem inválida')
                continue
            destino = input('Moeda de destino ex (BRL,EUR,USD):  ').strip().upper()
            if not destino or len(destino) != 3:
                print('Erro: moeda inválida (use 3 letras, ex: USD)')
                continue
            valor = leiafloat('valor: ')
            if valor <= 0:
                print('Digite um número maior do que 0.')
                continue

            resposta = conversao_taxa(valor, origem, destino)
            if resposta is None:
                print('Erro ao converter a moeda')
            else:
                print(f"{valor} {origem} → {resposta:.2f} {destino} (salvo no histórico )")
                lista.append({
                    'moeda_origem': origem,
                    'moeda_destino': destino,
                    "valor_conversão": valor,
                    "valor_convertido": resposta,
                    'data': data_hora_br
                })
                salvar(lista)

        elif opcao == 2:
            moedas_disponiveis()

        elif opcao == 3:
            ver_historico(lista)

        elif opcao == 4:
            if lista:
                resp = confirmar_acao("Quer continuar? [S/N]")
                if resp == 'N':
                    print('Manteremos o estado atual do seu arquivo.')
                else:
                    lista.clear()
                    print('O historico foi limpo com sucesso!')
                    salvar(lista)
            else:
                print('Não há nada para limpar no historico!')

        elif opcao == 5:
            lista_ordenada = ordenar_historico()
            if lista_ordenada is None:
                print('Não há nada para mostrar')
            else:
                ver_historico(lista_ordenada)

        elif opcao == 6:
            origem = input('Moeda de origem ex (BRL,EUR,USD): ').strip().upper()
            destino = input('Moeda de destino ex (BRL,EUR,USD): ').strip().upper()
            filtro = filtrar_moeda(origem, destino)
            if not filtro:
                print(f'nenhum filtro encontrado para {origem} ou {destino}')
            else:
                ver_historico(filtro)

        elif opcao == 7:
            salvar(lista)
            cabecalho("Saindo do sistema . . .")
            break

        else:
            print('Opção inválida!')


if __name__ == "__main__":
    main()
