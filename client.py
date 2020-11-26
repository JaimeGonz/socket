import socket

def main():
  msgFromClient= "Hola servidor UDP"
  bytesToSend= str.encode(msgFromClient)
  serverAddressPort= ("127.0.0.1", 20001)
  bufferSize= 1024


  #Crea un Socket UDP del lado del Cliente
  UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

  #Enviar al servidor usando el Socket UDP creado
  UDPClientSocket.sendto(bytesToSend, serverAddressPort)

  msgFromServer = UDPClientSocket.recvfrom(bufferSize)

  msg = "Mensaje del servidor {}".format(msgFromServer[0])
  print(msg)

if __name__ == "__main__":
  main()
