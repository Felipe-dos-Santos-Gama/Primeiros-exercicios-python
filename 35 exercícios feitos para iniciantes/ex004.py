#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possíveis sobre ele.

msg = input('Olá! Digite algo: ')
cores = {'magenta': '\033[35m', 'limpa': '\033[m'}
print('\033[35mQue tipo primitivo é:\033[m ', type(msg))
print('\033[35mSó tem espaço?\033[m', (msg.isspace()))
print('\033[35mÉ um número?\033[m', (msg.isnumeric()))
print('\033[35mÉ alfabético?\033[m', (msg.isalpha()))
print('\033[35mÉ alfanumérico?\033[m', (msg.isalnum()))
print('\033[35mSomente maiúsculas?\033[m', (msg.isupper()))
print('\033[35mSomente minúsculas?\033[m', (msg.islower()))
print('\033[35mEstá capitalizada?\033[m', (msg.istitle()))



'''
teste = input('Digite algo: ')
print('O tipo primitivo é: ', type(teste))
print(f'É número decimal? {teste.isdecimal()}')
print('É somente letra maiúscula? ', teste.isupper())
print('É alfabético? ', teste.isalpha())
print('É um alfanumérico? ', teste.isalnum())
print('É numérico? ', teste.isnumeric())
print('É somente letra minúscula? ', teste.islower())
print('É somente espaço? ', teste.isspace())
print('Está capitalizada? ', teste.istitle())
'''

'''
msg = input('Digite algo: ')
print('O tipo primitivo é: ', type(msg))
print(f'É apenas número? {msg.isnumeric()}')
print('É apenas letra? {} '.format(msg.isalpha()))
print('É apenas letra minúscula? ', msg.islower())
'''




