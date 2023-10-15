''' Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas. '''

cores = {'limpa': '\033[m', 'azul': '\033[34m'}
km = float(input('{}Olá! Qual a distância da viagem?{} '.format(cores['azul'], cores['limpa'])))
perto = km * 0.50
longe = km * 0.45
if km <= 200:
    print('A viagem de {}km ficará no valor de R${:.2f}.'.format(km, perto))
else:
    print('A viagem de {}km ficará no valor de R${:.2f}.'.format(km, longe))





'''
distancia = float(input('Olá! Qual a distância da sua viagem em Km? '))
print('Você está prester a iniciar uma viagem de {}km!' .format(distancia))
if distancia <= 200:
    preço = 0.50 * distancia
else:
    preço = 0.45 * distancia
print('Sua viagem ficou no valor de R${:.2f}.'.format(preço))
'''

#   preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45     # IF SIMPLIFICADO
#   print('Sua viagem de saiu no valor de R${:.2f}. Tenha uma boa viagem!'.format(preço))