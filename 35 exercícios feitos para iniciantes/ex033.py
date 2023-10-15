''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor. '''

a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if a > b and a > c:
    print('O número {} é o maior.'.format(a))
if b > a and b > c:
    print('O número {} é o maior.'.format(b))
if c > a and c > b:
    print('O número {} é o maior.'.format(c))
if a < b and a < c:
    print('O número {} é o menor.'.format(a))
if b < a and b < c:
    print('O número {} é o menor.'.format(b))
if c < a and c < b:
    print('O número {} é o menor.'.format(c))


'''
um = int(input('Digite o primeiro número: '))
dois = int(input('Digite o segundo número: '))
tres = int(input('Digite o terceiro número: '))
# VERIFICANDO O MAIOR
maior = um
if dois > um and dois > tres:
    maior = dois
if tres > um and tres > dois:
    maior = tres
# VERIFICANDO O MENOR
menor = um
if dois < um and dois < tres:
    menor = dois
if tres < um and tres < dois:
    menor = tres
print('O número {} é maior.'.format(maior))
print('O número {} é menor.'.format(menor))
'''


'''
if um > dois and um > tres:
    print('O número {} o é MAIOR dentre os três.'.format(um))
if dois > um and dois > tres:
    print('O número {} o é MAIOR dentre os três.'.format(dois))
if tres > um and tres > dois:
    print('O número {} é o MAIOR dentre os três.'.format(tres))

if um < dois and um < tres:
    print('O número {} é o MENOR dentre os três.'.format(um))
if dois < um and dois < tres:
    print('O número {} é o MENOR dentre os três.'.format(dois))
if tres < um and tres < dois:
    print('O número {} é o MENIOR dentre os três.'.format(tres)) 
'''

