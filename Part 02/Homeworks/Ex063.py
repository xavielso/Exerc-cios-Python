numero = int(input('Digite um numero: '))
atual = 1
anterior = 1
antecessor = 0
contador = numero
print('0 1 ', end='')
while not contador == 1:
    print(atual, end=' ')
    antecessor = anterior
    anterior = atual
    atual = anterior + antecessor
    contador -= 1
print('Fim', end='')



























