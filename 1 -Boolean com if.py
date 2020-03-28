#boolean = true e false são valores Boolean

idade = int(input('Qual é a sua idade: '))
if idade >= 18:
    print("Já pode dirigir")
    
else:
    print('Não pode dirigir')
# Exemplo de Boolean:

pode = idade >= 18
print(pode)

if idade >= 20 and idade <= 60: # or = ou
    print("Você está entre 20 e 60")
else:
    print("Você não está entre 20 e 60")
