matriz = [[0,0,0],[0,0,0],[0,0,0]]
par =impar= scol = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('digite um numero:'))
print('_'*30)
for l in range(0,3):
    scol += matriz[l][2]
    for c in range(0,3):
        print(f'{matriz[l][c]:^5}', end=' ')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        else:
            impar += matriz[l][c]
        if c == 0:
            mai = matriz[1][c]
        else:
            mai = matriz[1][c]
    print()

print('_'*30)
print(f'Soma dos valores pares: {par}')
print(f'Soma de valores Impar:{impar}')
print(f'Soma dos valores da tecerira coluna:{scol}')
print(f'Maior numero da segunda linha: {mai}')