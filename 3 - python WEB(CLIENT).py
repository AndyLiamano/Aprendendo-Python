from socket import *
import time

# dados do cliente para conexão com o server
serverHost = '127.0.1' # quando deixo sem informação, ele pega o IP da maquina
serverPort = 30800 # use valores acima de 10.000
mensagem = [b'ola, bem vindo!']

# cria o objeto socket e conectar ao servidor
sockobj = socket(AF_INET, SOCK_STREAM) #(Protocolo (IP), Servidor (TCP)) <= TCP-IP

sockobj.connect((serverHost, serverPort))
for linha in mensagem:
    sockobj.send(linha)
    
    #Resposta do servidor
    data = sockobj.recv(1024)# ???
    for c in range(1,10):
        print('Cliente Recebeu:', data)
sockobj.close()


#Testando a conexão com o servidor
'''
while True:
    conexao, endereco = sockobj.accept()
    print('O servidor esta conectado por', endereco)
    while True:
        data = conexao.recv(1024) # configurado para recebe 1024 bits de conexão
        if not data:
            break
        conexao.send(b'Eco=>' + data) # b'Eco=>' é da documentação
    conexao.close()
'''
