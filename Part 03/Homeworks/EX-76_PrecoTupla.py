tupla =('lapis', 2.00,
        'caderno', 5.00,
        'borracha',0.76,
        'laizeira',5.00,
        'apontador', 4.00,
        'mochila', 12.00,)
print(f'{"Listagem de preços":^40}')
for pos in range(0,len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end=' ')

    else:
        print(f'R${tupla[pos]:>5}')