numero = int(input('Digite um numero: '))
numeros = 0
total = 0
while numero != 999:
    numero = int(input('Digite um numero: '))
    if not numero == 999:
        numeros += 1
        total = total + numero
print('Voce digitou {} numeros e teve o total de {}.'.format(numeros, total))
