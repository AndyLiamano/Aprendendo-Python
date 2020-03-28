import random

a = random.randint(0,999)
b = random.randint(0,999)

soma = a + b    # Soma
mult = a * b    # Multiplicação
div = a / b     # Divisão
sub = a - b     # Subtração
divint = a // b # Parte inteiro da divisão
pot = a ** b    # Potência
resdiv = a % b  # Resto da divisão

nome = str(input('Qual é seu nome?\n'))

print('Prazer em te conhecer {}!'.format(nome))
print('Primeiro EX:{:20}!'.format(nome))
print('Segundo EX:{:>20}!'.format(nome))
print('Terceiro EX:{:^20}!'.format(nome))
print('Quarto EX:{:=^20}!'.format(nome))
print('Quinto EX: ''Oi'+'olá')
print('Sexto EX: ','Oi'*5)
print('Setimo EX: ','='*20)

print('O primeiro valor é {} e o segundo valor é {}'.format( a, b))
print('A soma é {}, a multiplicação é {} e a divisão é {:.3f}'.format(soma, mult, div), end=' >>> ')
print('Subtração é {}'.format(sub))





