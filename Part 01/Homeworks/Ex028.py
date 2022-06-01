from random import randint
print('Escreva um numero entre 0-5.')
numero = int(input('Digite um numero: '))
computador = randint(0, 5)
if numero == computador:
    print('Voce venceu, voce escreveu {} e o computador pensou em {}.'.format(numero, computador))
else:
    print('Voce perdeu, voce escreveu {} mas o computador pensou em {}.'.format(numero, computador))
