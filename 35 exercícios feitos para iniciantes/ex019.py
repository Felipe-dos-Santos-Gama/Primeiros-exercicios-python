# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
from time import sleep
cores = {'neutra': '\033[m', 'azulnegrito': '\033[1;34m', 'verde': '\033[32m', 'amareloepreto': '\033[4;33;40m'}
print('Irá acontecer um sorteio de quem irá apagar o quadro. Digite os nomes:')
a = str(input('{}Nome:{} '.format(cores['verde'], cores['neutra'])))
b = str(input('{}Nome:{} '.format(cores['verde'], cores['neutra'])))
c = str(input('{}Nome:{} '.format(cores['verde'], cores['neutra'])))
d = str(input('{}Nome:{} '.format(cores['verde'], cores['neutra'])))
lista = (a, b, c, d)
sorteado = choice(lista)
input('{}TECLE ENTER PARA SORTEAR E AGUARDE.{}'.format(cores['azulnegrito'], cores['neutra']))
sleep(1)
print('{}O nome sorteado foi:{} {}{}{}'
      .format(cores['verde'], cores['neutra'], cores['amareloepreto'], sorteado, cores['neutra']))










'''
import random
n1 = input('O primeiro aluno: ')
n2 = input('O segundo aluno: ')
n3 = input('O terceiro aluno: ')
n4 = input('O quarto aluno: ')
nomes = [n1, n2, n3, n4]
sorteio = random.choice(nomes)
input('TECLE ENTER PARA SORTEAR.')
print('O nome sorteado para apagar o quadro foi: {}.'.format(sorteio))
'''