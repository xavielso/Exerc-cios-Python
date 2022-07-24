from random import randint
lista = list()
jogos = list()
total = 1
print('    JOGO NA MEGA CENA     ')
print('_'*30)
quant = int(input('Digite a quantidade:'))
while total<=quant:
    cont = 0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total +=1

for i,l in enumerate(jogos):
    print(f'Jogos:{i+1 }: {l}')