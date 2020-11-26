import socket

def main():

  localIP = "127.0.0.1"
  localPort = 20001
  bufferSize = 1024

  msgFromServer = "Hola cliente UDP"
  bytesToSend = str.encode(msgFromServer)

  #Crea un socket de datagramas
  UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

  #Vincularse a la dirección e IP
  UDPServerSocket.bind((localIP, localPort))

  print("El servidor está listo y escuchando...")

  #Escucha para los datagramas entrantes
  while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Mensaje para el Cliente: {}".format(message)
    clientIP = "Dirección IP del Cliente: {}".format(address)

    print(clientMsg)
    print(clientIP)

    #Enviar respuesta al cliente
    UDPServerSocket.sendto(bytesToSend,address)

if __name__ == "__main__":
  main()
