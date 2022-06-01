peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = (peso / (altura * altura))
if imc < 18.5:
    print('O seu IMC foi de {:.2f}.'.format(imc))
    print('Você está na classificação MAGREZA.')
elif 18.5 >= imc <= 24.9:
    print('O seu IMC foi de {:.2f}.'.format(imc))
    print('Você está na classificação NORMAL.')
elif 25.0 >= imc <= 29.9:
    print('O seu IMC foi de {:.2f}.'.format(imc))
    print('Você está na classificação SOBREPESO de 1° grau.')
elif 30.0 >= imc <= 39.9:
    print('O seu IMC foi de {:.2f}.'.format(imc))
    print('Você está na classificação SOBREPESO de 2° grau.')
elif imc > 40.0:
    print('O seu IMC foi de {:.2f}.'.format(imc))
    print('Você está na classificação SOBREPESO de 3° grau.')

