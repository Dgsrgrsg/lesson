import socket

HOST = "127.0.0.1"
PORT = 20005
bufferSize = 1024
msgFromServer = "Hello World!"
bytesToSend = str.encode(msgFromServer)
# Создаю сокет на сервере
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Жду коннект
UDPServerSocket.bind((HOST, PORT))
# Выведу в консоль отладку, что ожидаю подключение
print("UDP server up and listening")
# Слушаю порт
while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    # Отправлю ответ клиенту (для проверки)
    UDPServerSocket.sendto(bytesToSend, address)
