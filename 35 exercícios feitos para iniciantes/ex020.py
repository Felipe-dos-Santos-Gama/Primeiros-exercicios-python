# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça
# um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a = str(input('Nome: '))
b = str(input('Nome: '))
c = str(input('Nome: '))
d = str(input('Nome: '))
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de nomes sorteada será: {}'.format(lista))
















'''
from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem sorteada será: ')
print(lista)
'''