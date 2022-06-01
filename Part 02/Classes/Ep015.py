# o comando break forca a saido do while em qualquer parte do codigo
# pode ser usado para interromper lacos infinitos ou finitos

numero = total = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    total += numero
print(f'A soma vale {total}.')

# nome = 'Vinicius'
# idade = '20'
# print(f'O {nome} tem {idade} anos.') # PYTHON 3.6+
# print('O {} tem {} anos.'.format(nome, idade)) # PYTHON 3
# print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2
