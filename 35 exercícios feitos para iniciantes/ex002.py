''' Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas. '''

print('*****' * 20)
nome = str(input('Olá, aluno! Digite o seu nome completo: '))
print('*****' * 20)
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'vermelhopreto': '\033[7;31;40m'}
print('Seja bem-vindo à Polícia Civil do Estado do Rio de Janeiro, {}{}{}!'.format(cores['azul'], nome, cores['limpa']))


'''
nome = input('Digite o seu nome: ')
print('Seja muito bem-vindo, {}!'.format(nome))

nome = input('Por favor, digite o seu nome: ')
print('Olá,', nome, ', seja bem-vindo.')
'''

