# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.


from math import radians, sin, cos, tan
cores = {'neutra': '\033[m', 'magenta': '\033[35m'}
num = float(input('{}Digite o valor do ângulo:{} '.format(cores['magenta'], cores['neutra'])))
angulo = radians(num)
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print('O ângulo de {} tem como SENO valor de {:.2f}.'.format(num, seno))
print('O ângulo de {} tem como COSSENO valor de {:.2f}.'.format(num, cosseno))
print('O ângulo de {} tem como TANGENTE valor de {:.2f}.'.format(num, tangente))


'''
import math
num = float(input('Digite o ângulo desejado: '))
rad = math.radians(num)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print('O ângulo de {} tem o seno de {:.2f}.'.format(num, seno))
print('O ângulo de {} tem o cosseno de {:.2f}.'.format(num, cosseno))
print('O ângulo de {} tem o tangente de {:.2f}.'.format(num, tangente))'''

'''
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo desejado para cálculo: '))
seno = sin(radians(angulo))   # EXPLICAÇÃO: angulo convertido para radianos, e depois calcular o seno dele
print('O ângulo {} tem o seno de {:.2f}.'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, tangente)) '''