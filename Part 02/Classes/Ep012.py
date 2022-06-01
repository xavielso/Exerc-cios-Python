# aninhar é colocar alguma coisa dentro da outra

# if (condição):
    # bloco 1
# elif (condição 2):
    # bloco 2
# else:
    # bloco 3

nome = str(input('Qual seu nome? '))

if nome == 'Vinicius':
    print(f'Que belo nome, tenha um bom dia {nome}')
elif nome == 'Joao' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem comum, olá {}'.format(nome))
elif nome in 'Ana Cláudia Jessica Quesia':
    print('Que belo nome feminino, tenha um bom dia {}'.format(nome))
# else é opcional
else:
    print('Tenha um bom dia {}'.format(nome))
