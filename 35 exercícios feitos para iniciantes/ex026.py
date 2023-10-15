''' Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. '''


frase = str(input('Olá! Digite uma frase qualquer: ')) .strip() .upper()
vezes = frase.count('A')
primeira = frase.find('A')
ultima = frase.rfind('A')
print('A letra "A" aparece {} vezes.'.format(vezes))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(primeira+1))
print('A letra "A" aparece pela última vez na posição {}.'.format(ultima+1))





'''
frase = str(input('Digite uma frase: ')).strip().upper()
print('Quantas vezes aparece a letra "a" na frase: {}'.format(frase.count('A')))
print('Em que posição aparece a primeira vez a letra "a": {}'.format(frase.find('A')+1))
print('Em que posição aparece a letra "a" pela última vez: {}'.format(frase.rfind('A')+1))
'''

#a = frase.count('a')
#pos = frase.find('a')
#ult = frase.rfind('a')