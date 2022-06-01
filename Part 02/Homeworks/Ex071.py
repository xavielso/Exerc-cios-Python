from math import floor
contador = int(input('Digite o valor a ser sacado: R$'))
while True:
    if ((contador / 50) > 0) and (contador > 50):
        print(f'Total de {(floor(contador / 50))} cedulas de R$50.')
        contador -= (floor(contador / 50)) * 50
    if ((contador / 20) > 0) and (contador > 20):
        print(f'Total de {(floor(contador / 20))} cedulas de R$50.')
        contador -= (floor(contador / 20)) * 20
    if ((contador / 10) > 0) and (contador > 10):
        print(f'Total de {(floor(contador / 10))} cedulas de R$10.')
        contador -= (floor(contador / 10)) * 10
    if ((contador / 1) > 0) and (contador > 1):
        print(f'Total de {(floor(contador / 1))} cedulas de R$1.')
        contador -= (floor(contador / 1))
