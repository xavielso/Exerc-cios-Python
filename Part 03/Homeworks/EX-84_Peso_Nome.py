listabase = list()
pessoa =list()

maior = menor = 0
while True:
    listabase.append(str(input('Nome da pessoa:')))
    listabase.append(float(input('Peso:')))

    pessoa.append(listabase[:])
    if len(pessoa) == 0:
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1]<menor:
            menor = pessoa[1]
    listabase.clear()

    brek = str(input('Deseja continuar:[S/N]'))

    if brek in 'nN':
        break

print('_'*30)
for i in pessoa:
    print(f'Nome:{i[0]}, Peso:{i[1]}')
    if i[1] == maior:
        print(f'Maiores pessos:{i[0]}')
print(f'Quantidade de cadastro {len(pessoa)}')