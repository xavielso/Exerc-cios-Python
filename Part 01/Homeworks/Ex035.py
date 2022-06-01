segmento1 = int(input('Digite o valor do primeiro segmento: '))
segmento2 = int(input('Digite o valor do segundo segmento: '))
segmento3 = int(input('Digite o valor do terceiro segmento: '))
if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3:
    print('Os segmentos acima podem formar um triangulo.')
else:
    print('Os segmentos acima nao podem formar um triangulo.')
