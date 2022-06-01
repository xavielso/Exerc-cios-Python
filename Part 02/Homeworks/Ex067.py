numero = 1
while numero > 0:
    numero = int(input('Digite um numero: '))
    if numero < 1:
        break
    for c in range(1, 11):
        print(f'{numero} * {c} == {(numero*c)}')