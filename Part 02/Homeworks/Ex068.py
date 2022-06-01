from random import randint
numero = 0
computador = 0
vitoria = 0
while True:
    numero = int(input('Digite um numero: '))
    opcao = str(input('Par ou Impar? [P/I]: ')).upper()
    computador = randint(1, 10)
    print(f'Voce jogou {numero} e o computador {computador}, o total foi de {(numero + computador)},', end=' ')
    if (numero + computador) % 2 == 0:
        if opcao == 'P':
            print('que é par.', end=' ')
            print('Voce venceu!')
            print('Vamos jogar novamente ...')
            print('')
            vitoria += 1
        else:
            print('que é par.', end=' ')
            print('Voce perdeu!')
            print(f'Voce venceu {vitoria} vez(es).')
            print('')
            break
    else:
        if opcao == 'I':
            print('que é impar.', end=' ')
            print('Voce venceu.')
            print('Vamos jogar novamente ...')
            print('')
            vitoria += 1
        else:
            print('que é impar.', end=' ')
            print('Voce perdeu.')
            print(f'Voce venceu {vitoria} vez(es).')
            print('')
            break
