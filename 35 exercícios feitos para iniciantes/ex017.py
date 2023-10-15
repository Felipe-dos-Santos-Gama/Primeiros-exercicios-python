# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
# um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

cores = {'neutro': '\033[m', 'magenta': '\033[35m', 'amarelo': '\033[33m'}
print('Calcule e mostre o comprimento da hipotenusa de um triângulo retângulo.')
co = float(input('{}Cateto oposto:{} '.format(cores['magenta'], cores['neutro'])))
ca = float(input('{}Cateto adjacente:{} '.format(cores['magenta'], cores['neutro'])))
formula = (co * co) + (ca * ca)     # FÓRMULA: a² = b² + c²
hipotenusa = pow(formula, (1/2))
print('A {}hipotenusa{} será de {}{}{}.'
      .format(cores['amarelo'], cores['neutro'], cores['amarelo'], hipotenusa, cores['neutro']))






'''
import math
cateto_oposto = float(input('Digite o numero do cateto oposto: '))
cateto_adjacente = float(input('Digite o número do cateto adjacente: '))
hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)
print('O comprimento da hipotenusa é {:.2f}.'.format(hipotenusa))
'''

'''
cateto_oposto = float(input('Digite o numero do cateto oposto: '))
cateto_adjacente = float(input('Digite o número do cateto adjacente: '))
hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}.'.format(hipotenusa))'''
