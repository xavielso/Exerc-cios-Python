primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
contagem = 0
while contagem < 10:
    print('{} '.format(termo), end='')
    termo += razao
    contagem += 1
print('Fim!')
