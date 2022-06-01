numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
opcao = -1

while opcao != 0:
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Verificar Maior')
    print('4 - Digitar novos numeros')
    print('')
    print('0 - Sair do programa')
    opcao = int(input('Digite uma opcao: '))

    if opcao == 1:
        print('A soma de {} com {} teve o resultado {}.'.format(numero1, numero2, (numero1 + numero2)))
    elif opcao == 2:
        print('A multiplicacao de {} com {} teve o resultado {}.'.format(numero1, numero2, (numero1 * numero2)))
    elif opcao == 3:
        if numero1 > numero2:
            print('O maior numero é o {}.'.format(numero1))
        else:
            print('O maior numero é o {}.'.format(numero2))
    elif opcao == 4:
        numero1 = int(input('Digite o primeiro numero: '))
        numero2 = int(input('Digite o segundo numero: '))

