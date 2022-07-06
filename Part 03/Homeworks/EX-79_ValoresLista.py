numero =  list ()
while True:
    n = int(input('Digite seu numero:'))
    if n not in numero:
        numero.append(n)
        print('valor add com sucesso...')
    else:
        print('valor já add não vou add')
    r = str(input('Quer continuar?[S/N]'))

    if r in 'nN':
        break
print('_'*30)
numero.sort()
print(f'voce digitou os numeros do menor para o maior {numero}')