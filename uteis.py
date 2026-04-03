import json
from json import JSONDecodeError

def confirmar_acao(msg):
    """
    Solicita ao usuário uma confirmação do tipo 'S' (sim) ou 'N' (não).

    Exibe a mensagem fornecida e repete a solicitação até que o usuário
    digite uma resposta válida ('S' ou 'N').

    Parâmetros:
    ----------
    msg : str
        Mensagem exibida para o usuário solicitando confirmação.

    Retorna:
    -------
    str
        'S' se o usuário confirmar ou 'N' se o usuário recusar.
    """
    while True:
        resp = str(input(msg)).strip().upper()
        if resp in ('S','N'):
            return resp


def leiaint(msg):
    """
    Solicita ao usuário a entrada de um número inteiro.

    Continua solicitando enquanto a entrada não for um inteiro válido.

    Parâmetros:
    ----------
    msg : str
        Mensagem exibida ao usuário solicitando o número inteiro.

    Retorna:
    -------
    int
        Número inteiro fornecido pelo usuário.
    """
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Erro! Digite um número inteiro!')


def leiafloat(msg):
    """
    Solicita ao usuário a entrada de um número decimal (float).

    Continua solicitando enquanto a entrada não for um float válido.

    Parâmetros:
    ----------
    msg : str
        Mensagem exibida ao usuário solicitando o número decimal.

    Retorna:
    -------
    float
        Número decimal fornecido pelo usuário.
    """
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('Erro! Digite um número float!')


def carregar():
    """
    Carrega o histórico de conversões armazenado em 'history.json'.

    Se o arquivo não existir ou estiver vazio/corrompido, retorna uma lista vazia.

    Retorna:
    -------
    list
        Lista de registros de histórico de conversão. Cada item é um dicionário.
    """
    try:
        with open("history.json", "r", encoding="utf-8") as arq:
            return json.load(arq)
    except (FileNotFoundError, JSONDecodeError):
        return []


def salvar(lista):
    """
    Salva o histórico de conversões em 'history.json'.

    Substitui o conteúdo anterior do arquivo pelo conteúdo atual da lista.

    Parâmetros:
    ----------
    lista : list
        Lista de registros de histórico de conversão a ser salva. Cada item é um dicionário.

    Retorna:
    -------
    None
    """
    with open("history.json", "w", encoding='utf-8') as arq:
        json.dump(lista, arq, ensure_ascii=False, indent=4)