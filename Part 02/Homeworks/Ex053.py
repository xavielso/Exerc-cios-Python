frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == frase:
    print('Temos um palindromo!')
else:
    print('A frase nao é um palindromo.')