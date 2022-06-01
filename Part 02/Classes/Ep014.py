# o laco for é utilizado quando se sabe o final das coisas
# while pode ser utilizado para fazer operacoes mesmo nao sabendo quando ira terminar, umas lista por exemplo
# o while so vai terminar quando a operacao for verdadeira
# sempre que a condicao for verdadeira o laco ira se repetir

numero = 1
par = impar = 0
while numero != 0:
    # bloco 1
    numero = int(input('Digite um numero: '))
    # bloco 2
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    # bloco 3
# ao terminar o laco o print é executado
print('Voce digitou {} numeros pares e {} numeros impares.'.format(par, impar))

