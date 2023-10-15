''' Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa
deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep
cores = {'limpa': '\033[m', 'verde': '\033[4;32m', 'vermelho': '\033[4;31m', 'azul': '\033[1;34m', 'azulepreto': '\033[34;40m'}
num = int(input('Olá! Tente acertar o número entre 0 a 5: '))
sorteio = randint(1, 5)
print('{}SORTEANDO O NÚMERO...{}'.format(cores['azulepreto'], cores['limpa']))
sleep(1)
print('{}Número {}!{}'.format(cores['azul'], sorteio, cores['limpa']))
if num == sorteio:
    print('{}Parabéns! Você acertou o número.{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Que pena! Você errou!{}'.format(cores['vermelho'], cores['limpa']))








'''
from random import randint
from time import sleep
print('**' * 30)
print('Olá! Tente acertar o número de 0 a 5.')
print('**' * 30)
chute = int(input('Chute o número: '))      # Jogador tenta acertar o número
print('PROCESSANDO...')
sleep(2)
numero = randint(0, 5)      # Computador PENSA em um número
print(numero)
if chute == numero:
    print('Parabéns! Você acertou o número.')
else:
    print('Que pena! Você errou.')
'''