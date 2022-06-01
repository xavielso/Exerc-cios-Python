opcao = genero = ''
idade = maiores = menores = 0
homem = 0
while True:
    idade = int(input('Digite uma idade: '))
    genero = str(input('Digite um genero[M/F]: ').upper())
    print('')
    if idade > 18:
        maiores += 1
    if genero == 'M':
        homem += 1
    elif idade < 20:
        menores += 1
    opcao = str(input('Deseja continuar[S/N]: ').upper())
    if opcao == 'N':
        break
print(f'O total de pessoas com mais de 18 anos foi de {maiores} pessoa(s).')
print(f'Tendo o total de homens cadastrados de {homem}, e com {menores} mulher(es) com menos de 20 anos.')
