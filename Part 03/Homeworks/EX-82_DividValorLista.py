lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite seu numero:')))
    fica = str(input('Quer continuar? [S/N]'))
    if fica in 'Nn':
        break

for i,v in enumerate(lista):
    if v % 2 ==0:
        par.append(v)
    elif v% 2 ==1:
        impar.append(v)
print(f'lista é: {lista}')
print(f'lista par é: {par}')
print(f'lista impar é: {impar}')