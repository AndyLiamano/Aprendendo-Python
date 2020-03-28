# Importando classes

import math
import random
# Primeiro usa o modulo antes do ponto e depois o comando.
a = random.randrange(0,999)
print(a)
print('\n')
a = math.cos(a)
print(a)
print('\n')

# random usa numeros aleatorios
# random.randrange e random.randint são semenlhantes.
for i in range (20):
    a = random.randint(0,999)
    print(a, end=' / ')
