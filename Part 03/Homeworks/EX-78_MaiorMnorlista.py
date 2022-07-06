lista= []
mai = 0
men = 0
for i in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {i}: ')))
    #if i ==0:
#        mai = men = lista[i]
 #   else:
    #      if lista[i] > mai:
    #       mai = lista[i]
    #   if lista[i] < men:
#       men = lista[i]

print('=-'*30)
print(f'Você digitou os valores {lista}')
print(f'Maior valor digitado: {max(lista)}; Posoção', end=' ')
for c,v in enumerate(lista):
    if v == max(lista):
        print(f'{c}...',end=' ')
print(f'\nMaior valor digitado: {min(lista)}; Posição:',end=' ')
for a,b in enumerate(lista):
    if b == min(lista):
        print(f'{a}...',end=' ')