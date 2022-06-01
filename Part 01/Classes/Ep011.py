# o padrao de cores usado no terminal por padrao é o ANSI (escape sequence)
# o codigo ANSI comeca com contrabarra seguido de \033[ e pode ser fechado com a letra m -> \033[m
# entre o colchete e a letra m fica o codigo da cor, podendo conter de um a tres codigos de cores
# sendo o primeiro codigo o do comportamento(style), seguido por ponto e virgula o segundo codigo é o do texto(text)
# seguido por outro ponto e virgula o ultimo é o fundo(background).

print('\033[0;33;44m Olá mundo!')

# codigos para estilo(1):
# 0 none
# 1 bold
# 4 underline
# 7 negative

# codigos para cor do texto(2):
# 30 - 37

# codigos para cores de background(3):
# 40 - 47
