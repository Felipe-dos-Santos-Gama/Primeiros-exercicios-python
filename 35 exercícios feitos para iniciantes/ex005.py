# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('\033[35mDigite um número:\033[m '))
cores = {'limpa': '\033[m', 'verde': '\033[32m', 'azul': '\033[34m', 'amarelo': '\033[33m', 'magenta': '\033[35m'}
sucessor = n1 + 1
antecessor = n1 - 1
print('Número digitado: {}{}{}. \nO seu sucessor é {}{}{}. \nO antecessor é {}{}{}.'
      .format(cores['amarelo'], n1, cores['limpa'],
              cores['azul'], sucessor, cores['limpa'],
              cores['azul'], antecessor, cores['limpa']))







'''
n1 = int(input('Digite um número: '))
#print('O seu sucessor é {}'.format(n1+1))
#print('O seu antecessor é {}'.format(n1-1))
print('O número {} tem como seu antecessor o {} e seu sucessor o {}.'.format(n1, n1-1, n1+1))
'''