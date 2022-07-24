ficha = list()

while True:
    nome = str(input('Nome do anulo:'))
    nota1= float(input('Nota1:'))
    nota2 = float(input('Nota2:'))
    media = ((nota1+nota2)/2)
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar?S/N'))
    if resp in 'Nn':
        break
print('_'*30)
print(f'{"No.":<4}{"Nome":<10}{"MÉDIA":>8}')
print('_'*30)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('_' * 30)
    opc = int(input('Mostrar notas de qual aluno:(999 interompe)'))
    if opc== 999:
        print('Finzalizado')
        break
    if opc <= len(ficha):
        print(f'notas de {ficha[opc][0]} são {ficha[opc][1]}')