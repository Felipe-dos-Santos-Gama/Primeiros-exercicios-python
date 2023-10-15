''' Crie um programa que leia o nome completo de uma pessoa e mostre:
- o nome com todas as letras maiúsculas
- o nome com todas as letras minúsculas
- quantas letras no total (sem considerar espaços)
- quantas letras tem o primeiro nome '''

nome = str(input('Digite um nome completo: ')) .strip()
print('Maiúsculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))
print('Seu nome tem um total de {}'.format(len(nome) - nome.count(' ')))  # diminui a quantidade de espaços
primeiro = nome.split()
print('Seu primeiro nome é {} e possui {} letras.'.format(primeiro[0], len(primeiro[0])))




'''
nome = str(input('Olá, digite seu nome completo: ')).strip()
print('Nome todo com letras maiúsculas: {}.'.format(nome.upper()))
print('Nome todo com letras minúsculas: {}.'.format(nome.lower()))
#print('Quantidade de letras ao total, sem contar espaços: {}.'.format(len(nome.replace(' ', ''))))
print('Quantidade de letras ao total: {}.'.format(len(nome) - nome.count(' ')))
#print('Quantidade de letras que tem o seu primeiro nome: {}.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} que possui {} letras.'.format(separa[0], len(separa[0])))
'''