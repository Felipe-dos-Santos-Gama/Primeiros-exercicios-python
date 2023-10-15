''' Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.''' # IMPRIMIR

cores = {'limpa': '\033[m', 'azul': '\033[34m'}

nome = str(input('Digite o nome de uma cidade: ')) .strip()
if nome.split()[0].upper() == 'SANTO':
    print('O nome da cidade COMEÇA com SANTO.')
else:
    print('A cidade NÃO começa com SANTO.')



'''
# EXERCICIO CORRETO (um comentário no youtube)
cidade = str(input('Em qual cidade você mora? ')).strip()
if (cidade.split()[0].upper() == 'SANTO'):
    print(f'A sua cidade {cidade} começa com o nome Santo')
else:
    print(f'A sua cidade {cidade} não começa com o nome Santo')
'''



#cidade = str(input('Diga o nome de uma cidade: ')).strip()
#print(cidade[0:6].lower() == 'santo')

