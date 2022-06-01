from random import randint
numero = randint(1, 10)
jogada = -1
palpite = 0

print(numero)
print('O computador pensou em um numero.')
while jogada != numero:
    jogada = int(input('Digite um numero: '))
    palpite += 1
print('Voce venceu, porem teve que usar {} chances.'.format(palpite))