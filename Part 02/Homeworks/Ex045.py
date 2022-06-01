from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('As suas opções de jogada são: pedra, papel ou tesoura.')
jogador = str(input('Digite a sua jogada: ').lower())
print('O jogador escolheu {}, e o computador {}.'.format(jogador, itens[computador]))

if (computador == 0 and jogador == 'pedra') or (computador == 1 and jogador == 'papel') or (computador == 2 and jogador == 'tesoura'):
    print('O jogo empatou.')
elif (computador == 0 and jogador == 'tesoura') or (computador == 1 and jogador == 'pedra') or (computador == 2 and jogador == 'papel'):
    print('O computador venceu, mais sorte na proxima.')
elif (computador == 0 and jogador == 'papel') or (computador == 1 and jogador == 'tesoura') or (computador == 2 and jogador == 'pedra'):
    print('Você venceu, parabens.')
