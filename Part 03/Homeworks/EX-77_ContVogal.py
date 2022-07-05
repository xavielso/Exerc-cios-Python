palavra =('cachorro','gato','aviao','mariana','thiago','maria',)

for n in palavra:
    print(f'\n Na palavra {n.upper()} temos:', end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')