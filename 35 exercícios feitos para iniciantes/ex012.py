# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

cores = {'limpa': '\033[m', 'azul': '\033[34m', 'verde': '\033[32m'}
valor = float(input('{}Olá! Digite o valor do produto:{} '.format(cores['azul'], cores['limpa'])))
print('O valor do produto é de R${:.2f}.'.format(valor))
desconto = valor * (5/100)
total = valor - desconto
print('O valor do produto que custa R${:.2f}, com um desconto de 5% passará a ser {}R${:.2f}{}.'
      .format(valor, cores['verde'], total, cores['limpa']))




'''
produto = float(input('Digite o valor do preço de certo produto: R$ '))
desconto = produto * 5/100
print('O produto com desconto de 5%, com esse desconto de R${},'.format(desconto),end='')
resultado = produto - desconto
print(' ele está saindo a R${}.'.format(resultado))
'''

'''
preço = float(input('Digite o valor do produto: R$'))
novo = (preço*5/100)
desconto = preço - novo
print('O produto com valor de R${:.2f}, com de 5% passará a ser R${:.2f}.'.format(preço, desconto))
'''

'''
exemplos de porcentagem: 
10*5/100 = 5% de 10
1500*10/100 = 10% de 1500
875*15/100 = 15% de 875
'''