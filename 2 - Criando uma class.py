# Autor: Anderson CS

class Andy:
    def __init__(teste, n, i):
        teste.nome = n
        teste.ano = i
        print('Teste de chamada')

    def imprime(teste):
        print('Olá meu nome é {} e nasci em {}'.format (teste.nome, teste.ano))

x = str(input('Seu nome: '))
y = int(input('Ano que Nasceu: '))

A = Andy(x,y)
A.imprime()




    
        
