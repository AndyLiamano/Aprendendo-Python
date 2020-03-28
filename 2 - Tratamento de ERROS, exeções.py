class valor(Exception):

    def __init__(self, n):
        self.num = n

    
    def __str__(self):
        return'Numero {} repitido'.format(self.num)

def main():
    lista = []
    for i in range(10):
        while True:  # ???
            try: # Tratamento de erro
                num = int(input('Digite um numero: '))
                break
            except ValueError: # Menssagem de de Erro!
                print('Digite apenas numeros')

        if num not in lista: 
            lista.append(num) # Adiciona no final, o valor digitado.
            print(lista)
        else:
            raise valor(num)
        # raise ???
        # fique atento com letras maiusculas e minusculas

main()

  
