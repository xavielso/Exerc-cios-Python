'''aluno = dict()

aluno['nome'] = str(input('Digite o Nome:'))
aluno['nota1'] = float(input('Digite a Primeira nota:'))
aluno['nota2'] = float(input('Digite a Segunda nota:'))
print('_'*30)
aluno['media']  = (aluno["nota1"] + aluno["nota2"])/2
Meu jeito de fazer
#print(f'Média do aluno {aluno["nome"]} é {(aluno["nota1"] + aluno["nota2"])/2}')
#if (aluno["nota1"] + aluno["nota2"])/2 >= 6:
#    print('Parabens você passou')
#else:
#    print('Cagada em vei, vai ficar para o próximo ano')

if aluno['média'] >=7:
    aluno['situação'] = 'aprovado'
elif aluno['média'] >=5:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')
'''
aluno= dict()
listaluno = list()

while True:
    aluno['nome'] = str(input('Digite o Nome:'))

    aluno['nota 1'] = float(input('Digite a Primeira nota:'))
    aluno['nota 2'] = float(input('Digite a Segunda nota:'))
    aluno['media'] = (aluno["nota 1"] + aluno["nota 2"]) / 2
    if aluno['media'] >= 7:
        aluno['situação'] = 'aprovado'
    elif aluno['media'] >= 5:
        aluno['situação'] = 'recuperação'
    else:
        aluno['situação'] = 'reprovado'
    listaluno.append(aluno.copy())

    fica = str(input('Deseja cadastrar outro?S/N'))
    if fica in 'Nn':
        break
print('_'*30)
for e in listaluno:
    for k,v in e.items():
        print(f'{k}: {v}')
    print()
