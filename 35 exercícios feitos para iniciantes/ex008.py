# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

cores = {'limpa': '\033[m', 'amarelo': '\033[33m', 'azul': '\033[34m'}
num = float(input('{}Olá! Digite um número para ser convertido:{} '.format(cores['azul'], cores['limpa'])))
#print('A medida de {}{}m{} pode ser convertida em: '.format(cores['amarelo'], num, cores['limpa']))
mm = num * 100
cm = num * 100
dm = num * 10
dam = num / 10
hm = num / 100
km = num / 1000
print('{}A medida de {}m, pode ser convertida em:{} {}mm, {}cm, {}dm, {}dam, {}hm, {}km.'
      .format(cores['azul'], num, cores['limpa'], mm, cm, dm, dam, hm, km))


'''
print('{}mm'.format(mm))
print('{}cm'.format(cm))
print('{}dm'.format(dm))
print('{}dam'.format(dam))
print('{}hm'.format(hm))
print('{}km'.format(km)) '''


'''
medida = float(input('Digite um valor em metros, para ser convertido: '))
#print('Valor convertido para centímetros é {} centímetros.'.format(medida*100))
#print('Valor convertido para milímetros é {} milímetros'.format(medida*1000))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('O valor de {}metros tem: \n{}km, {}hm, {}dam, {}dm, {:.0f}cm, {:.0f}mm.'
      .format(medida, km, hm, dam, dm, cm, mm))
'''