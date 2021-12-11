import socket, threading

LOCALHOST = 'localhost'
PORT = 4444

class Server(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("Nova conexão adicionada ", clientAddress)

    def run(self):
        message = ''
        print("Conexão de:  ", clientAddress)
        while True:
            data = self.csocket.recv(2048)
            message = data.decode()
            if message == "quit":
                break
            elif message.startswith('echo '):
                message = message.split('echo ',1)
                if len(message) == 2:
                    message = message[1]
                    if message == '':
                        message = ' '
            print("Mensagem do cliente: ", message)
            self.csocket.send(bytes(message,'UTF-8'))
        


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Servidor online")
while True:
    server.listen()
    clientsock, clientAddress = server.accept()
    newthread = Server(clientAddress, clientsock)
    newthread.start()