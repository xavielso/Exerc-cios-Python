maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('{} -> Digite seu peso: '.format(c)))
    if peso > maior:
        maior = peso
    elif peso < menor or menor == 0:
        menor = peso
print('O maior peso registrado foi de {}kg, enquanto o menor foi de {}kg.'.format(maior, menor))