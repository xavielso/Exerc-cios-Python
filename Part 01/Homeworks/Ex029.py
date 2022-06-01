numero = int(input('Digite um numero: '))
if numero > 80:
    print('Voce ultrapassou {}Km/h acima do limite de velocidade permitido, '.format((numero - 80)), end='')
    print('e por conta disso vai receber uma multa de R${}.'.format(((numero - 80) * 7)))
else:
    print('Voce nao ultrapassou o limite de velocidade permitido.')