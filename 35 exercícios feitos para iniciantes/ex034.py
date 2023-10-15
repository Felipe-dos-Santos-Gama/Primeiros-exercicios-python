''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%. '''

cores = {'limpa': '\033[m', 'verde': '\033[32m', 'amarelo': '\033[33m'}
salario = float(input('{}Olá! Quanto é o seu salário?{} '.format(cores['amarelo'], cores['limpa'])))
maior = (salario * (10/100)) + salario
menor = (salario * (15/100)) + salario
if maior > 1250:
    print('Seu salário é R${:.2f} e você receberá um {}aumento de 10%{} indo para o valor de R${:.2f}.'
          .format(salario, cores['verde'], cores['limpa'], maior))
else:
    print('Seu salário é de R${:.2f} e você receberá um {}aumento de 15%{} indo para o valor de R${:.2f}.'
          .format(salario, cores['verde'], cores['limpa'], menor))










'''
salario = float(input('Olá! Quanto é o seu salário: '))
aumento10 = salario + salario * 10/100
aumento15 = salario + salario * 15/100
if salario > 1250:
    print('Recebendo um salário de R${:.2f}, com um aumento de 10% irá para R${:.2f}.'.format(salario, aumento10))
if salario <= 1250:
    print('Recebendo um salário de R${:.2f}, com um aumento de 15% irá para R${:.2f}.'.format(salario, aumento15))
'''