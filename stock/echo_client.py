import socket

msgFromClient       = "Hello World!"
bytesToSend         = str.encode(msgFromClient)
HOST   = ("127.0.0.1", 20005)
bufferSize          = 1024
# Создаю UDP сокет на клиенте
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Отправляю сообщение серверу через созданый сокет
UDPClientSocket.sendto(bytesToSend, HOST)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Сообщение от сервера {}".format(msgFromServer[0])

print(msg)
