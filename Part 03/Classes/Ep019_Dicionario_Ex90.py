'''pessoas = {'Nome':'thiago', 'Sexo':'M','Idade':20}
print(pessoas['Nome'])
print('_'*30)
print(pessoas.keys())
print('_'*30)
print(pessoas.values())
print('_'*30)
print(pessoas.items())
print('_'*30)
for k in pessoas.values():
    print(k)
print('_'*30)
for k in pessoas.keys():
    print(k)
print('_'*30)
# del pessoas['Sexo']
pessoas['Nome'] = 'leandro'
pessoas['peso'] = 65.9
for k, j in pessoas.items():
    print(f'{k} ={j}')

brasil = []
estado = {'uf':'Santa catarina','sigla':'SC'}
estado2 = {'uf':'Rio Grande do sul','sigla':'RS'}
brasil.append(estado)
brasil.append(estado2)
print(brasil)
print('_'*30)
print(brasil[0])
print('_'*30)
print(brasil[0]['uf'])
print('_'*30)
print(brasil[1]['sigla'])'''

estados = dict()
brasil = list()

for c in range (0,3):
    estados['uf'] = str(input('Unidade Federativa:'))
    estados['sigla'] = str(input('Sigla do estado:'))
    brasil.append(estados.copy())
'''for e in brasil:
    for v,k in e.items():
        print(f'o campo {v} tem o valor {k}')'''
for e in brasil:
    for v in e.values():
        print (v, end= ' ')
    print()
