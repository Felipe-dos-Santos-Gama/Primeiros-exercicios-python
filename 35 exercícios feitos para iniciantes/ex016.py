# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

#import math
from math import trunc
cores = {'neutra': '\033[m', 'magenta': '\033[35m', 'pretoevermelho': '\033[30;41m'}
num = float(input('{}Olá! Digite um número real:{} '.format(cores['magenta'], cores['neutra'])))
#resposta = math.trunc(num)
resposta = trunc(num)
print('O valor digitado {} tem como número inteiro {}{}{}.'
      .format(num, cores['pretoevermelho'], resposta, cores['neutra']))










'''from math import trunc
real = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}.'.format(real, trunc(real)))'''

'''
num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}.'.format(num, int(num))) '''