ano = int(input('Digite o ano em que estamos: '))
if ano % 4 == 0 and ano % 100 != 100:
    print('Este é um ano bissexto')
else:
    print('Este nao é um ano bissexto')
