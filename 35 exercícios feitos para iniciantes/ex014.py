# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cores = {'limpa': '\033[m', 'amarelo': '\033[33m', 'vermelho': '\033[31m'}
celsius = float(input('Diga qual a temperatura em graus celsius: '))
conversao = celsius * 1.8 + 32
print('A temperatura de {}{:.1f}°C{} convertido será de {}{:.1f}°F{}.'
      .format(cores['amarelo'], celsius, cores['limpa'], cores['vermelho'], conversao, cores['limpa']))


# Equação:
# °F = (°C * 1.8) + 32
# or
# °F = °C * 9 / 5 + 32  -> pois 9 / 5 = 1.8


'''
celsius = float(input('Digite a temperatura em graus celsius: '))
#temperatura = celsius * 1.8 + 32
temperatura = 9 * celsius / 5 + 32
print('A temperatura de {:.1f}°C convertida para fahrenheit é de {:.1f}°F.'.format(celsius, temperatura))
'''

# Fórmula da conversão de celsius para fahrenheit:
# F = ((9 * c) / 5) + 32