# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar.

cores = {'limpa': '\033[m', 'verde': '\033[32m', 'vermelho': '\033[31m', 'ciano': '\033[36m'}
din = float(input('{}Olá! Diga quanto você tem na sua carteira para fazer a conversão:{} '
                  .format(cores['ciano'], cores['limpa'])))
dolar = din / 5.17
euro = din / 5.45
print('Você tem {}RS{:.2f}{}. Pode comprar: {}\n{:.2f}US$ \n{:.2f}EUR{}.'
      .format(cores['vermelho'], din, cores['limpa'], cores['verde'], dolar, euro, cores['limpa']))






'''
dinheiro = float(input('Digite quanto de dinheiro você tem na sua carteira: R$ '))
print('Você pode comprar ${:.2f} com R${}. '.format(dinheiro/4.93, dinheiro))
'''
'''
real = float(input('Digite quanto de dinheiro você tem na sua carteira: R$'))
dolar = real / 4.99
euro = real / 5.34
peso = real * 70.2098
print('Com R${:.2f} você pode comprar $ {:.2f}.'.format(real, dolar))
print('Com R${:.2f} você pode comprar EUR {:.2f}.'.format(real, euro))
print('Com R${:.2f} você pode comprar ARS {:.2f}.'.format(real, peso))
'''