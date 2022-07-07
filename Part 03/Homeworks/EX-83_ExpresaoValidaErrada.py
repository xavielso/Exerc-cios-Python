expre = str(input('Digite a expressão:'))
pilha=[]
for sim in expre:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('expressão está certa')
else:
    print('tá errada.')