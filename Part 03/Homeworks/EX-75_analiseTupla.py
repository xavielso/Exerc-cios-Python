numero = (int(input('Primeiro numero:')),int(input('Segundo numero:')),
          int(input('Terceiro numero:')),int(input('Ultimo numero:')))
print(f'voce digitou os valores: {numero}')
print(f'o valor 9 apareceu {numero.count(9)} VEZES')
if 3 in numero:
    print(f'o valor 3 apareceu na {numero.index(3)+1} POSIÇÃO')
else:
    print('valor 3 não foi digitado')
for n in numero:
    if n %2 ==0:
        print(n, end=' ')