primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
contagem = 0
maximo = 10
while contagem < maximo:
    print('{} '.format(termo), end='')
    termo += razao
    contagem += 1
    if contagem == maximo:
        print('PAUSA')
        maximo = int(input('Digite quantos termos voce quer: '))
        maximo += contagem
print('Progressao finalizada com {} termos mostrados.'.format(contagem))
