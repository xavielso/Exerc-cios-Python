salario = float(input('Digite o valor do seu salario: R$'))
if salario > 1250:
    print('Com base no seu salario de R${}, tera um aumento de 10%,'.format(salario), end=' ')
    print('sendo assim ira ficar com o total de R${}'.format((((salario * 0.10) + salario))))
if salario < 1250:
    print('Com base no seu salario de R${}, tera um aumento de 15%,'.format(salario), end=' ')
    print('sendo assim ira ficar com o total de R${}'.format((((salario * 0.15) + salario))))
