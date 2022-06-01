numero = int(input('Digite um número: '))
print('1 - Para binario')
print('2 - Para octal')
print('3 - Para hexadecimal')
escolha = int(input('Qual sera a base de conversão? '))

if escolha == 1:
    print('O valor em binario ficou {}.'.format(bin(numero)))
elif escolha == 2:
    print('O valor em octal ficou {}.'.format(oct(numero)))
elif escolha == 3:
    print('O valor em hexadecimal ficou {}.'.format(hex(numero)))
else:
    print('Você deve escolher uma opção valida!')