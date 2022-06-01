valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Em quantos anos você deseja pagar? '))

if (valor / (anos * 12)) > (salario * 0.30):
    print('O valor da parcela ficou R${:.2f}, está acima do valor maximo'.format((valor / (anos * 12))))
    print('que é de R${:.2f} para {} anos, recomendamos que você aumente'.format((salario * 0.30), anos))
    print('o número de parcelas.')
elif (valor / (anos * 12)) < (salario * 0.30):
    print('O valor da parcela ficou R${:.2f}, está dentro do seu limite'.format((valor / (anos * 12))))
    print('Seu credito foi aprovado!')

