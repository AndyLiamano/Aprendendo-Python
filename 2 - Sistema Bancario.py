class conta:
    def __init__(self,ID, saldo):
        self.ID = ID
        self.saldo = saldo

    def __str__(self):
        return 'ID: {}\nSaldo: R$ {:.2f}'.format(self.ID, self.saldo)

    def __add__(self,outro):
        self.saldo += outro.saldo

    def __sub__(self, sub):
        self.saldo -= sub.saldo
        
Bradesco = conta(456,3000)
print(Bradesco)

Itau = conta(555,2000)
print(Itau)
Itau + Bradesco # Quem tiver a Esquerda, recebera o valor da Direita com a __add__
Bradesco + Itau
print(Itau.saldo)
print(Bradesco.saldo)


