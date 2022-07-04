tunum = ('zero','um','dois','três','quatro','cinco',
          'seis','sete','oito','nove', 'dez')

while True:
    num = int(input('Digite seu numero: 0 a 10 '))
    if 0 <= num <= 10:
        print(f'numero digitado foi: {tunum[num]}')
        conta = str(input('quer continuar?[S/N] '))
    if conta in 'nN':
        break