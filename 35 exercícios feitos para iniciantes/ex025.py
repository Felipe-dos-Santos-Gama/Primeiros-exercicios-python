''' Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome. ''' # IMPPRIMIR

nome = str(input('Olá! Digite o seu nome todo: ')) .strip()
a = 'SILVA' in nome.upper().split()
print('O nome tem SILVA? {}'.format(a))





# EXERCÍCIO EXPLICADO (comentário no youtube)
#nome = str(input('Qual o seu nome? ')).strip()
#print('Seu nome possui "SILVA"? {}'.format('SILVA' in nome.upper().split()))


#nome = str(input('Digite o seu nome completo: ')).strip()
#print('Seu nome tem SILVA? {}'.format('SILVA' in nome.upper()))
