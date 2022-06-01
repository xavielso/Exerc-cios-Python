nome = preco = opcao = menornome = ''
total = maior = menor = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o preco do produto: R$tt'))
    total += preco
    if preco > 1000:
        maior += 1
    if menor == 0 or preco < menor:
        menor = preco
        menornome = nome
    opcao = str(input('Deseja continuar[S/N]: ').upper())
    print('')
    if opcao == 'N':
        break
print(f'O total gasto na compra foi de R${total}.')
print(f'Tendo {maior} produto(s) que custam assima de mil reais, e o nome do produto mais barato foi a {menornome}.')
