def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('erro! digite um número inteiro!')


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('erro! digite um número float!')
