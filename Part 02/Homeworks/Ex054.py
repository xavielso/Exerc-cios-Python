maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('{} -> Digite seu ano de nascimento: '.format(c)))
    if (2021 - nascimento) >= 18:
        maior += 1
    else:
        menor += 1
print('Ao total foram {} pessoas maiores de idade e {} pessoas menores de idade.'.format(maior, menor))


