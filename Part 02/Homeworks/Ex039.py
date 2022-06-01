ano = int(input('Digite seu ano de nascimento: '))
idade = 2020 - ano

if idade < 18:
    print('Você devera se alistar no futuro, ainda faltam {} anos'.format((18 - idade)))
    print('para o seu alistamento.')
elif idade == 18:
    print('Você deve se alistar neste mesmo ano.')
elif idade > 18:
    print('Você já deveria ter realizado o alistamento')
    print('já se passaram {} anos.'.format((idade - 18)))

