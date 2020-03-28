class Teste3:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        print('Hello World!')

    def cadastro(self):
        self.nome = input('Nome: ')
        self.ano = input('Ano que nasceu: ')
        

    def exibir(self):
        print('Nome: {:20}'.format(self.nome))
        print('Ano de nascimento: {:20}'.format(self.ano))

        
      
T = Teste3('Brian', 1997)
T.cadastro()
T.exibir()
'''
class Teste4():
    def __init__(self, nome, ano, cidade):
        super(Teste4, self).__init__(nome, ano)
        self.cidade = cidade
        print(1567)
        print('Cidade: {}'.format(self.cidade))

cidade = input('Nome da cidade: ')       
Teste4(self.nome,self.ano, cidade)
'''
 
            
