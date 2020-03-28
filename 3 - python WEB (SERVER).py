from socket import *

# dados da conexão com servidor
meuHost = '127.0.1' # quando deixo sem informação, ele pega o IP da maquina
minhaPort = 30800 # use valores acima de 10.000
sockobj = socket(AF_INET, SOCK_STREAM) #(Protocolo (IP), Servidor (TCP)) <= TCP-IP

sockobj.bind((meuHost, minhaPort))

sockobj.listen(5) # Limite de conexão por vez

#Testando a conexão com o servidor

while True:
    conexao, endereco = sockobj.accept()
    print('O servidor esta conectado por', endereco)
    while True:
        data = conexao.recv(1024) # configurado para recebe 1024 bits de conexão
                #??? linha a cima.
        if not data:
            break
        conexao.send(b'Eco=>' + data) # b'Eco=>' é da documentação
    conexao.close()

