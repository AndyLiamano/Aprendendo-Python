Teste = {'Nome': '', 'Ano':'' }
print(Teste ['Nome'])

class Teste2:
    pass

X = Teste2() # Obrigatorio!

N = str(input('Nome:'))
A = int(input('Ano de nasc:'))

X.Nome = N
X.Ano = A

print(X.__dict__)
