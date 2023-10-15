# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2m².

cores = {'limpa': '\033[m', 'magenta': '\033[35m', 'verde': '\033[32m', 'azul': '\033[34m'}
largura = float(input('{}Quantos metros de largura tem a parede:{} '.format(cores['magenta'], cores['limpa'])))
altura = float(input('{}Quantos metros de altura tem a parede:{} '.format(cores['magenta'], cores['limpa'])))
area = altura * largura
print('A área da parede é de {}{}m²{}'.format(cores['azul'], area, cores['limpa']))
# cada litro de tinta = 2m²
tinta = area / 2
print('Será necessário {}{}L{} de tinta para pintar a parede.'.format(cores['verde'], tinta, cores['limpa']))


'''
altura = float(input('Digite quantos metros de altura te a parede: '))
largura = float(input('Digite quantos metros de largura tem a parede: '))
area = altura * largura
print('Sua parede tem uma dimensão de {}x{}. Sendo assim, a área dela é de {}m²'.format(altura, largura, area))
tinta = area / 2
print('Será necessário {} litros de tinta para pintá-la.'.format(tinta))
'''