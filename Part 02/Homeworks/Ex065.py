opcao = ''
maior = menor = media = total = 0
while opcao in 'S':
    numero = int(input('Digite um numero: '))
    total += 1
    media += numero
    if maior == 0 or numero > maior:
        maior = numero
    elif menor == 0 or numero < menor:
        menor = numero
    opcao = str(input('Deseja continuar[S/N]: ')).upper()
print('A media entre o(s) {} numero(s) digitado(s) foi de {}.'.format(total, (media/total)))
print('Sendo assim o maior numero digitado foi {}, enquanto o menor foi {}.'.format(maior, menor))

