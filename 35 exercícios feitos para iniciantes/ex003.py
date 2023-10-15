''' #Crie um programa que leia dois números e mostre a soma entre eles.'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
soma = n1 + n2
cores = {'verde': '\033[32m', 'amarelo': '\033[33m', 'limpa': '\033[m'}
print('A soma dos números {}{:.2f}{} + {}{:.2f}{} é igual a {}{:.2f}{}.'
      .format(cores['verde'], n1,
              cores['limpa'],
              cores['verde'], n2,
              cores['limpa'],
              cores['amarelo'], soma,
              cores['limpa']))





'''
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
r = n1 + n2
#print('O resultado da soma entre {} e {} é: {}' .format(n1, n2, r))
print ('O resultado da soma é: {} ' .format(r))
'''

'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
resultado = n1 + n2
print('{} + {} é igual a {}!'.format(n1, n2, resultado))
'''




