total = 0
for c in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        total += numero
print('O valor total somando os pares foi de {}.'.format(total))
