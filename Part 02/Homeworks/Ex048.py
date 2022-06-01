valor = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        valor += c
print('O valor total foi {}.'.format(valor))
