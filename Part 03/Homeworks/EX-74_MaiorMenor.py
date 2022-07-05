from  random import randint

numero = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
print(f'valores sorteados forão: ')
for n in numero:
    print(f'{n} ', end=' ')

print(f'\n maior valor sorteado foi: {max(numero)}')
print(f'\n maior valor sorteado foi: {min(numero)}')