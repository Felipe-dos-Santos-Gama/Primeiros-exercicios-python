# Faça um programa que leia um número inteiro e mostre na tela a sua tabuada.

num = int(input('Olá! Digite um número para ver sua tabuada: '))
cores = {'limpa': '\033[m', 'ciano': '\033[36m'}
print('*****' * 15)
print('{}A tabuada de {} é:{}'.format(cores['ciano'], num, cores['limpa']))
print('-' * 12)
print('{} x 1 = {}'.format(num, num*1))
print('{} x 2 = {}'.format(num, num*2))
print('{} x 3 = {}'.format(num, num*3))
print('{} x 4 = {}'.format(num, num*4))
print('{} x 5 = {}'.format(num, num*5))
print('{} x 6 = {}'.format(num, num*6))
print('{} x 7 = {}'.format(num, num*7))
print('{} x 8 = {}'.format(num, num*8))
print('{} x 9 = {}'.format(num, num*9))
print('{} x 10 = {}'.format(num, num*10))
print('-' * 12)










'''
n = int(input('Digite um número que será mostrado a tabuada do mesmo: '))
# print('A tabuada deste número é: '
#     '\n{}x{}={} \n{}x{}={} \n{}x3={} \n{}x4={} \n{}x5={} \n{}x6={} \n{}x7={} \n{}x8={} \n{}x9={} \n{}x10={}'
#      .format(n, 1, n*1,n ,2 ,n*2,n ,n*3,n ,n*4,n ,n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))
print('-' *12)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('-' *12)
'''