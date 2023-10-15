# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

cores = {'limpa': '\033[m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'vermelho': '\033[31m'}
nome = str(input('Diga o seu nome: '))
salario = float(input('Olá, {}! Diga quanto é o seu salário: '.format(nome)))
aumento = salario * (15/100)
reajuste = salario + aumento
print('Seu salário de {}R${:.2f}{} passará por um reajuste de 15% de aumento e passará a ser {}R${:.2f}{}.'
      .format(cores['vermelho'], salario, cores['limpa'], cores['amarelo'], reajuste, cores['limpa']))





'''
salario = float(input('Digite o seu salário: '))
print('O salário é de {} reais.'.format(salario))
print('O salário irá aumentar {} reais com o aumento de 15%.'.format(salario*15/100))

aumento = float((input)('Seu salário terá um aumento de {} reais com os 15% de aumento.'.format(salario*(15/100))))
resultado = salario + aumento
print('Com o aumento, salário é de {} reais.'.format(resultado))
'''
#salario = float(input('Digite quanto é o salário do funcionário: R$ '))
#aumento = salario * 15 / 100
#novo = salario + aumento
#print('O seu salário irá aumentar R${:.2f} com o aumento de 15% e irá para de R${:.2f}.'.format(aumento, novo))

#BÔNUS: Ler o preço de um produto, calcular o preço dele com desconto de 10% pra pagamento à vista, e com aumento
# de 4% para pagamento parcelado.
'''
produto = float(input('Informe o valor do produto: R$ '))
desconto = (produto * 10 / 100)
novo = produto - desconto
print('O produto no valor de R${} com desconto de 10%, pagando à vista, ficará no valor de R${:.2f}.'
      .format(produto, novo))
aumento = produto * 8 / 100
novo_aumento = produto + aumento
print('O produto no valor de R${} parcelado, com aumento de 8%, será de R${:.2f}'.format(produto, novo_aumento))
'''


