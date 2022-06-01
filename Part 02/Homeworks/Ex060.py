numero = int(input('Digite um numero: '))
fatorial = numero
resultado = 1

print('Calculando {}! = '.format(numero), end='')
while fatorial != 0:
    print('{} * '.format(fatorial), end='')
    resultado = resultado * fatorial
    fatorial -= 1
print('= {}'.format(resultado), end='')

