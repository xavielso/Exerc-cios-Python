lista =[]

while True:
    n = int(input('Digite numero:'))
    fica = str(input('Deseja continuar?[S/N]'))
    if fica in 'Nn':
        break
print(f'Você digitou {len(lista)}')
lista.sort(revarse=True)
print(f'Os valores em ordem decrecente {lista}')
if 5 in lista:
    print('5 esta na lista.')
else:
    print('5 não esta na lista')