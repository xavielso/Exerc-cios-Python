valor = float(input('Digite o valor do produto: R$'))
print('1 - À vista no dinheiro/cheque: 10% de desconto.')
print('2 - À vista no cartão: 5% de desconto.')
print('3 - Em até 2x no cartão: preço normal.')
print('4 - Em 3x ou mais no cartão: 20% de juros.')
tipo = int(input('Qual sera a forma de pagamento? '))

if tipo == 1:
    print('A forma de pagamento escolhida foi à vista no dinheiro/cheque.')
    print('O valor do produto foi de R${}, para R${} com os 10% de desconto.'.format(valor, (valor - (valor * 0.10))))
elif tipo == 2:
    print('A forma de pagamento escolhida foi à vista no cartão.')
    print('O valor do produto foi de R${}, para R${} com os 5% de desconto.'.format(valor, (valor - (valor * 0.05))))
elif tipo == 3:
    print('A forma de pagamento escolhida foi em até 2x no cartão.')
    print('O valor do produto foi de R${}, para R${} com os 0% de desconto.'.format(valor, valor))
elif tipo == 4:
    print('A forma de pagamento escolhida foi em 3x ou mais no cartão.')
    print('O valor do produto foi de R${}, para R${} com os 20% de acréscimo.'.format(valor, valor + (valor * 0.20)))
else:
    print('Digite uma opção valida.')
