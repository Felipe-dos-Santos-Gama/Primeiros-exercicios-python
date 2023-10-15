'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

cores = {'limpa': '\033[m', 'verde': '\033[32m', 'vermelho': '\033[31m', 'azul': '\033[34m'}
vel = float(input('Olá! Digite a quantos km/h o veículo estava: '))
multa = (vel - 80) * 7
if vel > 80:
    print('{}Velocidade máxima ultrapassada! Você passou a {}km/h e receberá uma multa no valor de RS{:.2f}.{}'
          .format(cores['vermelho'], vel, multa, cores['limpa']))
if vel <= 80:
    print('{}Você passou a {}km/h.{}'.format(cores['verde'], vel, cores['limpa']))
print('{}Dirija com segurança. E se beber, não dirija. Tenha uma boa viagem!{}'.format(cores['azul'], cores['limpa']))




'''
carro = int(input('Diga qual a velocidade que o carro estava: '))
if carro > 80:
    multa = (carro - 80) * 7
    print('Você passou a {}km/h e receberá uma multa de {}R$ por ultrapassar o máximo permitido.' .format(carro, multa))
print('======' * 15)
print('Dirija com segurança! Tenha uma boa viagem.'.format(carro))
'''
