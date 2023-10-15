#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
#  de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por
#  dia e R$0,15 por Km rodado.

cores = {'neutro': '\033[m', 'verdesublinhado': '\033[4;32m', 'magenta': '\033[35m', 'azulsublinhado': '\033[4;34m'}
distancia = float(input('{}Olá! Diga quantos km foram percorridos:{} '.format(cores['magenta'], cores['neutro'])))
dias = int(input('{}Quantos dias foi alugado:{} '.format(cores['magenta'], cores['neutro'])))
valor_dia = dias * 60
valor_hora = distancia * 0.15
total = valor_dia + valor_hora
print('Você percorreu {}{}km{} durante {} dia(s) de aluguel, e o valor ficou em {}R${:.2f}{}.'
      .format(cores['azulsublinhado'], distancia, cores['neutro'],
              dias, cores['verdesublinhado'], total, cores['neutro']))


'''
km = int(input('Diga a quantidade de kilômetro percorrido: '))
dias = float(input('Diga a quantidade de dias a qual o carro foi alugado: '))
aluguel = dias * 60
km_percorrido = km * 0.15
total = aluguel + km_percorrido
print('Foi percorrido {}km em {:.0f} dias/dia. O valor a pagar será de R${:.2f}. '.format(km, dias, total))
'''