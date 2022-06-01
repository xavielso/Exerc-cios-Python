# o bloco um so sera executado se a condicao for verdadeira
# se por acaso for negativa ele checa o elif, e se for negativo tambem
# o fim acaba sendo sempre o else se ele existir se nao, o codigo vai para fora do if.

# if (condição):
    # bloco 1
# elif (condição 2):
    # bloco 2
# else:
    # bloco 3

numero1 = float(input('Digite a primeira nota: '))
numero2 = float(input('Digite a segunda nota: '))
media = (numero1 + numero2)/2
print('A sua media foi {:.1f}'.format(media))
print('Aprovado' if media >= 6 else 'Reprovado')



