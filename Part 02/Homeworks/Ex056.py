media = 0
maiornome = ''
maior = 0
menor = 0

for c in range(1, 5):
    nome = str(input('{} -> Digite seu nome: '.format(c)))
    idade = int(input('{} -> Digite sua idade: '.format(c)))
    genero = str(input('{} -> Digite seu genero[M/F]: '.format(c)).upper())
    print(' ')

    media = media + idade
    if idade > maior and genero == 'M':
        maior = idade
        maiornome = nome
    if genero == 'F' and idade < 21:
        menor = menor+1
print('A media de idade do grupo foi de {} anos.'.format(media/4))
print('O nome do homem mais velho é {}.'.format(maiornome))
print('E {} mulheres sao menores de 21 anos.'.format(menor))
