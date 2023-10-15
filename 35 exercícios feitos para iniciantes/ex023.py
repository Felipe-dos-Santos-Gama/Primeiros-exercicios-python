''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

cores = {'neutra': '\033[m', 'amarelo': '\033[33m'}
num = int(input('{}Informe um número de 0 a 9999:{} '.format(cores['amarelo'], cores['neutra'])))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))





'''
numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {}...'.format(numero))
print('Unidade: {}'.format((u)))
print('Dezena: {}'.format((d)))
print('Centena: {}'.format((c)))
print('Milhar: {}'.format((m)))
'''

''' numero // 1 = x -> x // 10 = resto da divisão(módulo)  # 2023 / 1 = 2023 -> 2023 / 10 = 202,3
    numero // 10 = inteiro -> inteiro // 10 = módulo    # 2023 / 10 = 202,3 -> 202 / 10 = 20,2
    numero // 100 = inteiro -> inteiro // 10 = módulo   # 2023 / 100 = 20,23 -> 20 / 10 = 2,0
    número // 1000 = inteiro -> inteiro // 10 = módulo    # 2023 / 1000 = 2,023 -: 2 / 10 = 0,2 '''

# no vídeo da aula passa o "int" para "str".