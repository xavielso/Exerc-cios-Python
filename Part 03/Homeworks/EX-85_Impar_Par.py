'''''numero = list()
impar= list()
par = list()

while True:
    n = int(input('Ditite um numero:'))
    para = str(input('Deseja continuar?S/N'))
    if n %2 ==0 or n == 0:
        print('par')
        par.append(n)
    else:
        impar.append(n)
    if para in 'nN':
        break
impar.sort()
par.sort()
numero.append(par[:])
numero.append(impar[:])
print(f'Numeros impares em ordem crecente é: {numero[1]}')
print(f'Numeros pares em ordem crescente é: {numero[0]}')'''''

numero = [[],[]]
while True:
    n = int(input('Ditite um numero:'))
    para = str(input('Deseja continuar?S/N'))
    if n %2 ==0 or n == 0:
        numero[0].append(n)
    else:
        numero[1].append(n)
    if para in 'nN':
        break
numero[0].sort()
numero[1].sort()
print(f'Numeros impares em ordem crecente é: {numero[1]}')
print(f'Numeros pares em ordem crescente é: {numero[0]}')