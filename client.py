import socket,sys

SERVER = 'localhost'
PORT = 4444

if len(sys.argv) <= 2:
  print("Por favor use argumentos <Nome> <ip> ")
  sys.exit()

nameClient = sys.argv[1]
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
clientMessage = "Conectado"
client.sendall(bytes(clientMessage,'UTF-8'))
in_data =  client.recv(2048)
print("Mensagem para o servidor: " ,in_data.decode())
while True:
  clientMessage = input()
  if clientMessage == 'quit':
    break
  elif clientMessage.startswith('echo '):
    client.sendall(bytes(clientMessage,'UTF-8'))
    in_data =  client.recv(2048)
    print("Mensagem para o servidor: " ,in_data.decode())


client.close()