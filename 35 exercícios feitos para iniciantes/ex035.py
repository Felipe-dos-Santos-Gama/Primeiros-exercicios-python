''' Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo. '''

cores = {'limpa': '\033[m', 'azul': '\033[34m', 'vermelho': '\033[31m', 'verde': '\033[32m'}
a = float(input('{}Digite o valor da primeira reta: '.format(cores['azul'])))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta:{} '.format(cores['limpa'])))
if a + b > c and a + c > b and b + c > a:
    print('{}Os segmentos formam um triângulo.{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Os segmentos NÃO formam um triângulo.{}'.format(cores['vermelho'], cores['limpa']))





# "Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro."
# A soma do TERCEIRO segmento TEM que ser menor que a soma dos outros DOIS segmentos.
# DOIS SOMADOS um com o outro é maior que o terceiro número.

'''
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a + b > c and a + c > b and b + c > a:
    print('Formam um TRIÂNGULO.')
else:
    print('Não formam um TRIÂNGULO.')
'''