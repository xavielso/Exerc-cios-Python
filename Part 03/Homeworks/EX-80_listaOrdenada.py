#lista = list()
lista = []

for c in range(0,5):
    n = int(input('Digite seu numero: '))
    if c == 0 or n> lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n<= lista[pos]:
                lista.insert(pos,n)
                break
            pos +=1
print(f'os valores em ordem crecente é: {lista}')