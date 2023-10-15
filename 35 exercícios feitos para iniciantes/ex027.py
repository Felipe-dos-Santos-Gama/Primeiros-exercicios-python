''' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.'''

nome = str(input('Olá! Digite o seu nome completo: ')) .strip()
n = nome.split()
print('O seu primeiro nome é {}.'.format(n))
print('O seu último nome é {}.'.format(n[len(n)-1]))    # -1 porque o programa conta o 0. Ele tem um a menos.
                                                        # len de 'nome' porque sabe-se quantas posições tem 'nome'


'''
n = str(input('Digite o seu nome completo: ')) .strip()
print('Seu nome completo é {}.'.format(n))
nome = n.split()
print('O seu primeiro nome é {}.'.format(nome[0]))
print('O seu último nome é {}.'.format(nome[len(nome)-1]))
'''

'''
text = 'Essa, é, uma, string, de, teste'
rs1 = text.rsplit(',',1)
print(rs1)
'''