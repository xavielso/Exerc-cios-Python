distancia = int(input('Qual a distancia da viagem?: '))
if distancia > 200:
    print('O custo da passagem ficou R${}, por ser uma viagem acima de 200km foi cobrado R$0,45 por km.'.format((distancia * 0.45)))
else:
    print('O custo da passagem ficou R${}, por ser uma viagem acima de 200km foi cobrado R$0,50 por km.'.format((distancia * 0.50)))