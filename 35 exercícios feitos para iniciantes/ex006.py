# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
print('\033[30m-=-=-=-=\033[m' * 15)
num = int(input('\033[32mDigite um número:\033[m '))
print('\033[30m-=-=-=-=\033[m' * 15)
cores = {'limpa': '\033[m', 'amarelo': '\033[33m'}
dobro = num * 2
triplo = num * 3
raiz = pow(num, 1/2)
print('{}O dobro é:{} {}'.format(cores['amarelo'], cores['limpa'], dobro))
print('{}O triplo é:{} {}'.format(cores['amarelo'], cores['limpa'], triplo))
print('{}A raiz quadrada é:{} {:.2f}'.format(cores['amarelo'], cores['limpa'], raiz))


'''
n1 = int(input('Digite um número: '))
#print('O seu dobro é {}'.format(n1*2))
#print('O seu triplo é {}'.format(n1*3))
#print('A sua raiz quadrada é {}'.format(n1**(1/2)))
print('O dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrada de {} é {}.'.format(n1, n1*2,n1, n1*3,n1, n1**(1/2)))

#d = n1 * 2
#t = n1 * 3
#r = n1 ** (1/2)
#print('O dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrada de {} é {}.'.format(n1, d, n1, t, n1, r))
'''