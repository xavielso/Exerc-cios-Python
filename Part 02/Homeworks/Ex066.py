numero = soma = total = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma += numero
    total += 1
print(f'A quantia de numero(s) digitado(s) foi de {total}, e obtiveram o total de {soma}.')
