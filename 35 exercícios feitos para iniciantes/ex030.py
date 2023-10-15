''' Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. '''

cores = {'limpa': '\033[m', 'azul': '\033[34m'}
num = int(input('{}Digite um número para saber se ele é par ou ímpar:{} '.format(cores['azul'], cores['limpa'])))
if num % 2 == 0:
    print('Este número é PAR.')
else:
    print('Este número é ÍMPAR.')











'''
num = int(input('Digite um número: '))
resultado = num / 2 == 0  # num % 2
if num % 2 == 0:
    print('O número {} é par.' .format(num))
else:
    print('O número {} é ímpar.'.format(num))
'''

# EXPLICAÇÃO:
# numero % 2 -> "o 'resto' do número da divisão por 2"
'''
num = int(input('Digite um número aleatório: '))
resul = num % 2
if resul == 0:
    print('O número {} é par.' .format(num))
else:
    print('O número {} é ímpar.'.format(num))
'''