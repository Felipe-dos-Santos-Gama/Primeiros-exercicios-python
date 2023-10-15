''' Faça um programa que leia um ano qualquer e mostre se ele é bissexto. '''

from datetime import date
ano = int(input('Olá! Informe um ano qualquer: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 400 and ano % 100:
    print('O ano {} É BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é bissexto.'.format(ano))

# ser múltiplo de 400 e 100
# não pode ser divisível por 100, então não pode ser diferente de 0! -> ano % 100 != 0

'''
from datetime import date
ano = int(input('Olá! Digite um ano para a análise. Coloque 0 para o ano atual: '))
if ano == 0:
     ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} É BISSEXTO.'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO.'.format(ano))
'''