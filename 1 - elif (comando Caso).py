# elif é semelhante ao comando escolha/caso
print('Segunda-Feira (1)')
print('Terça-Feira (2)')
print('Quarta-Feira(3)')
print('Quinta-Feira(4)')
print('Sexta-Feira(5)')
print('Sábado(6)')
print('Domingo(7)')

semana = int(input('Digite um numero: '))

if semana == 1:
    print('Hoje é Segunda-Feira')
elif semana == 2:
    print('Hoje é Terça-Feira')
elif semana == 3:
    print('Hoje é Quarta-Feira')
elif semana == 4:
    print('Hoje é Quinta-Feira')
elif semana == 5:
    print('Hoje é Sexta-Feira')
elif semana == 6:
    print('Hoje é sábado')
elif semana == 7:
    print('Hoje é Domingo')
else:
    print('Numero errado!')

