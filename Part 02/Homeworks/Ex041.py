ano = int(input('Digite seu ano de nascimento: '))
idade = 2020 - ano

if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade <= 19:
    print('Sua categoria é JUNIOR.')
elif idade == 20:
    print('Sua categoria é SÊNIOR.')
elif idade > 20:
    print('Sua categoria é MASTER.')