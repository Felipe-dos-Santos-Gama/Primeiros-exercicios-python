# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a nota do 1º bim: '))
n2 = float(input('Digite a nota do 2° bim: '))
n3 = float(input('Digite a nota do 3° bim: '))
n4 = float(input('Digite a nota do 4° bim: '))
media = (n1+n2+n3+n4) / 4
cores = {'limpa': '\033[m', 'verde': '\033[32m', 'vermelho': '\033[31m'}
if media < 6:
    print('Resultado final: {}. {}Você ficou abaixo da média, precisará fazer recuperação.{}'
          .format(media, cores['vermelho'], cores['limpa']))
else:
    print('Resultado final: {}. {}Parabéns! Você está \033[4maprovado\033[m!{}'
          .format(media, cores['verde'], cores['limpa']))


'''
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
print('A média da nota deste aluno é {}'.format((nota1+nota2)/2))
'''

'''
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('A média deste aluno é {}.'.format(media))
'''