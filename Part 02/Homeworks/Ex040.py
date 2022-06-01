nota = float(input('Digite uma nota: '))
nota2 = float(input('Digite outra nota: '))

if ((nota + nota2) / 2) < 5:
    print('A sua média ficou {}, está abaixo do minimo.'.format(((nota + nota2) / 2)))
    print('Você foi reprovado(a).')
elif 5 <= ((nota + nota2) / 2) < 6.9:
    print('A sua média ficou {}, está mediana.'.format(((nota + nota2) / 2)))
    print('Você está em recuperação.')
elif ((nota + nota2) / 2) > 7:
    print('A sua média ficou {}, está na média.'.format(((nota + nota2) / 2)))
    print('Você foi aprovado(a).')
