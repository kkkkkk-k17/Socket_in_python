import socket

# Crearea unui obiect de tip socket pentru client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Atribuirea adresei IP și portului server-ului
server_address = ('127.0.0.1', 12345)

# Conectarea la server
client_socket.connect(server_address)

while True:
    # Introducerea mesajului de la tastatură
    message = input("Introduceti un mesaj: ")

    # Trimiterea mesajului la server
    client_socket.send(message.encode())

    # Primirea mesajelor de la server
    received_message = client_socket.recv(1024).decode()

    # Afisarea mesajelor primite de la server
    print("Mesaj primit de la server: " + received_message)