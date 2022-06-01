s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triangulo ', end='')
    if s1 == s2 == s3:
        print('Equilatero.')
    elif s1 != s2 != s3 != s1:
        print('Escaleno.')
    else:
        print('Isosceles.')
else:
    print('Os segmentos acima nao podem formar um triangulo')